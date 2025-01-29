from sensors.imu import SimulatedIMU, ArduinoIMU
from sensors.servo import Servo
import time

if __name__ == "__main__":
    # Setup
    imu = SimulatedIMU("data/sample_data.csv")
    # imu = ArduinoIMU("", baudrate=115200)
    yaw_servo = Servo("yaw")
    pitch_servo = Servo("pitch")

    # Loop
    while True:
        # Read from sensor
        imu.update()
        # pitch, roll, yaw
        angles = imu.get_angles()
        yaw_angle = angles[2]
        pitch_angle = angles[0]

        # Send command
        yaw_servo.write(yaw_angle)
        pitch_servo.write(pitch_angle)
