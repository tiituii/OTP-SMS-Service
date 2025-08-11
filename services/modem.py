import serial
import time
import threading

PORT = "/dev/ttyACM2"  # Change accordingly
BAUD = 115200
serial_lock = threading.Lock()

def send_sms(phone_number, message):
    try:
        ser = serial.Serial('/dev/ttyACM2', 115200, timeout=5)
        time.sleep(1)

        def send_at(cmd, delay=2):
            # print(f">>> {cmd}")
            ser.write((cmd + '\r').encode())
            time.sleep(delay)
            reply = ser.read_all().decode(errors='ignore')
            # print(reply)
            return reply
        send_at("AT+CMGF=1")
        # Send SMS
        send_at(f'AT+CMGS="{phone_number}"', delay=2)
        ser.write((message + '\x1A').encode())  # CTRL+Z = \x1A
        print("[Sent message, waiting for final response]")
        time.sleep(5)
        result = ser.read_all().decode(errors='ignore')
        ser.close()
        if "+CMGS" in result:
            return True, result
        else:
            return False, result

    except Exception as e:
        print("Error sending SMS:", e)
        return False
