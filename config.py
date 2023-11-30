from datetime import datetime

operating_rooms = {
    1: {"machines": ["MRI", "CT", "ECG"]},
    2: {"machines": ["CT", "MRI"]},
    3: {"machines": ["CT", "MRI"]},
    4: {"machines": ["MRI", "ECG"]},
    5: {"machines": ["MRI", "ECG"]}
}

doctor_requirements = {
    "heart_surgeon": {
        "required_machine": "ECG",
        "base_duration": 3,
    },
    "brain_surgeon": {
        "required_machine": "MRI",
        "base_duration": 2,
        "extended_duration": 3,
    }
}

or_availability = [(
    datetime.now().replace(
        hour=10,
        minute=0,
        second=0,
        microsecond=0,
    ),
    or_id,
) for or_id in operating_rooms]

