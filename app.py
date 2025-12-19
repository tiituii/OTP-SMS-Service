from flask import Flask, request, jsonify
from services.modem import send_sms
from utils.validators import validate_phone_number
import random
app = Flask(__name__)

@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json(force=True)
    phone = data.get("phone")
    if not phone :
        return jsonify({"status": "failed", "detail": "Missing phone "}), 400

    if not validate_phone_number(phone):
        return jsonify({"status": "failed", "detail": "Invalid phone number"}), 400
    random_otp = random.randint(100000, 999999)  # 6-digit random number
    msg = "Your OTP Code is : {}".format(random_otp)
    success, detail = send_sms (phone, msg) 
    print(success)
    if success:
        return jsonify({"OTP Code": str(random_otp),"status": "success", "detail": "OTP has been Sent!"})
    else:
        return jsonify({"status": "failed", "detail": detail}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)


