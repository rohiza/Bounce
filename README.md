
### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3
- Flask

### Installation

Follow these steps to set up your development environment:

1. **Install Flask**

   Flask can be installed using pip. In your terminal or command prompt, run:

   ```
   pip install flask
   ```

2. **Run the Scheduler Application**

   Navigate to the directory containing `scheduler.py` and run the following command:

   ```
   python scheduler.py
   ```

   This will start the Flask web server, with the application listening for requests.

## Usage

The application provides an API to request the next available OR slot for surgeries. Here are some examples of how to use the API:

### Requesting an OR Slot

#### For a Heart Surgeon

To request an OR slot for a heart surgeon, use the following `curl` command:

```bash
curl -X POST http://127.0.0.1:5000/request_slot \
     -H "Content-Type: application/json" \
     -d '{"doctor_type": "heart_surgeon"}'
```

#### For a Brain Surgeon

To request an OR slot for a brain surgeon, use this command:

```bash
curl -X POST http://127.0.0.1:5000/request_slot \
     -H "Content-Type: application/json" \
     -d '{"doctor_type": "brain_surgeon"}'
```

