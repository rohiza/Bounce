
import heapq
from datetime import datetime, timedelta

from flask import Flask, jsonify, request

from config import doctor_requirements, operating_rooms, or_availability

app = Flask(__name__)

heapq.heapify(or_availability)

END_OF_WEEK = datetime.now() + timedelta(days=7)

def calculate_surgery_duration(
    doctor_type,
    or_id,
):
    if doctor_type == "brain_surgeon" and "CT" not in operating_rooms[or_id]["machines"]:
        return doctor_requirements[doctor_type]["extended_duration"]

    return doctor_requirements[doctor_type]["base_duration"]


def find_next_available_slot(doctor_type):

    while or_availability:
        available_time, or_id = heapq.heappop(or_availability)

        if available_time > END_OF_WEEK:
            break

        end_of_day = available_time.replace(
            hour=18,
            minute=0,
            second=0,
            microsecond=0,
        )

        if available_time < end_of_day:
            if doctor_requirements[doctor_type]["required_machine"] in operating_rooms[or_id]["machines"]:
                surgery_duration = calculate_surgery_duration(doctor_type, or_id)
                surgery_end_time = available_time + timedelta(hours=surgery_duration)

                if surgery_end_time < end_of_day:
                    heapq.heappush(or_availability, (surgery_end_time, or_id))
                    return {
                        "or_id": or_id,
                        "time": available_time.strftime("%Y-%m-%d %H:%M"),
                    }

        next_day_start = (available_time + timedelta(days=1)).replace(
            hour=10,
            minute=0,
            second=0,
            microsecond=0,
        )
        heapq.heappush(or_availability, (next_day_start, or_id))

    return None

@app.route('/request_slot', methods=['POST'])
def request_slot():
    data = request.json
    doctor_type = data.get("doctor_type")

    if doctor_type not in doctor_requirements:
        return jsonify({"error": "Invalid doctor type"}), 400

    slot = find_next_available_slot(doctor_type)
    if slot:
        return jsonify(slot)
    else:
        return jsonify({"error": "No available slots"}), 404

if __name__ == '__main__':
    app.run(debug=True)
