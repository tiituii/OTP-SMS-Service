import serial
import time
import threading

PORT = "/dev/ttyUSB4"  # Change accordingly
BAUD = 115200
serial_lock = threading.Lock()

# def send_sms(phone_number, message):
#     try:
#         ser = serial.Serial(PORT, BAUD, timeout=5)
#         time.sleep(1)

#         def send_at(cmd, delay=2):
#             print(f">>> {cmd}")
#             ser.write((cmd + '\r').encode())
#             time.sleep(delay)
#             reply = ser.read_all().decode(errors='ignore')
#             return reply
#         send_at("AT+CMGF=1")
#         # Send SMS
#         send_at(f'AT+CMGS="{phone_number}"', delay=2)
#         ser.write((message + '\x1A').encode())  # CTRL+Z = \x1A
#         print("[Sent message, waiting for final response]")
#         time.sleep(5)
#         print(ser.read_all().decode(errors='ignore'))
#         result =' '
#         ser.close()
#         if "+CMGS" in result:
#             return True, result
#         else:
#             return False, result
        

#     except Exception as e:
#         print("Error sending SMS:", e)
#         return False
def send_sms(phone_number, message):
    

    ser = serial.Serial(PORT, BAUD, timeout=5)
    time.sleep(1)

    ser.reset_input_buffer()
    ser.reset_output_buffer()

    def read_until(expect, timeout=10):
        buf = ""
        end = time.time() + timeout
        while time.time() < end:
            if ser.in_waiting:
                buf += ser.read(ser.in_waiting).decode(errors="ignore")
                if expect in buf:
                    return buf
            time.sleep(0.1)
        return buf

    ser.write(b"ATE0\r")
    read_until("OK", 2)

    ser.write(b"AT+CMGF=1\r")
    read_until("OK", 2)

    ser.write(f'AT+CMGS="{phone_number}"\r'.encode())
    read_until(">", 5)          # ⬅️ WAIT FOR PROMPT

    ser.write((message + "\x1A").encode())

    result = read_until("+CMGS", 30)
    result += read_until("OK", 5)

    ser.close()
    print("RAW:", repr(result))

    return "+CMGS" in result, result
















# def send_sms(phone_number, message):
#     try:
#         ser = serial.Serial('/dev/ttyUSB3', 115200, timeout=1)
#         time.sleep(1)

#         def send_at(cmd, delay=1):
#             ser.write((cmd + '\r').encode())
#             time.sleep(delay)
#             return ser.read_all().decode(errors='ignore')

#         send_at("AT+CMGF=1")
#         send_at(f'AT+CMGS="{phone_number}"', delay=2)

#         ser.write((message + '\x1A').encode())  # CTRL+Z
#         print("[Sent message, waiting for final response]")

       
#         timeout = time.time() + 20   # GSM can be slow
#         result = ""
#         while time.time() < timeout:
#             if ser.in_waiting:
#                 result += ser.read(ser.in_waiting).decode(errors='ignore')

#             if "+CMGS" in result:
#                 break

#             time.sleep(0.2)

#         ser.close()
#         print(repr(result))  # DEBUG

#         if "+CMGS" in result:
#             return True, result
#         else:
#             return False, result

#     except Exception as e:
#         print("Error sending SMS:", e)
#         return False
