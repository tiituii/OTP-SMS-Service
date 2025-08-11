# OTP Sender API

A simple Python Flask-based API to send OTP (One-Time Password) codes to users' phone numbers in a specific format.

## Features
- Validate phone numbers using regex pattern.
- Generate a random 6-digit OTP code.
- Return OTP with a JSON response.
- Ready for integration with SMS gateways.

## Phone Number Format
The API validates phone numbers in the format:
```
+855XXXXXXXXX
```
Where `+855` is the country code and the rest are digits.  
Regex pattern used:
```
^\+855\d{8,9}$
```

## API Endpoint
**POST** `/send_otp`  
**Request Body** (JSON):
```json
{
  "phone": "+855101234567"
}
```

**Response**:
```json
{
  "OTP Code": 123456,
  "status": "success",
  "detail": "OTP has been Sent!"
}
```

## Installation
1. Clone this repository
```bash
git clone https://github.com/tiituii/otp-sender-api.git
cd otp-sender-api
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the server
```bash
python app.py
```

## Requirements
- Python 3.8+
- Flask

## License
This project is licensed under the MIT License.
