import serial

PORT = "COM3"          # change to your port
BAUD = 9600

# temp = 500 -> 0x01F4
frame = bytes([0xFE, 0xB2, 0x01, 0xF4, 0x00, 0xA7])

with serial.Serial(PORT, BAUD, timeout=1) as ser:
    ser.write(frame)
    response = ser.read(6)
    print("Sent:    ", frame.hex(" "))
    print("Received:", response.hex(" "))