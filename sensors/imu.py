from abc import ABC, abstractmethod
import numpy as np
import time
import serial


class IMU(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_roll(self):
        pass

    @abstractmethod
    def get_pitch(self):
        pass

    @abstractmethod
    def get_yaw(self):
        pass

    @abstractmethod
    def get_angles(self):
        pass


class SimulatedIMU(IMU):
    def __init__(self, data_file, noise=0.01):
        try:
            with open(data_file, "r") as fin:
                self.data = list(map(str.strip, fin.readlines()))
        except Exception as e:
            print(e)
            exit(1)
        self.noise = noise
        self.index = 0
        self.direction = 1
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0
        self.start = time.time()

    def update(self):
        self.index = self.index + (1 * self.direction)
        if self.index == len(self.data) - 1:
            self.direction = -1
        elif self.index == 0:
            self.direction = 1
        try:
            timestamp, self.roll, self.pitch, self.yaw = list(
                map(float, self.data[self.index].split(","))
            )
            self.roll += np.random.normal(0, self.noise)
            self.pitch += np.random.normal(0, self.noise)
            self.yaw += np.random.normal(0, self.noise)
        except Exception as e:
            print(self.data[self.index])
            print(e)
            exit(1)
        while time.time() - self.start < timestamp:
            time.sleep(0.0001)

    def get_roll(self):
        return self.roll

    def get_pitch(self):
        return self.pitch

    def get_yaw(self):
        return self.yaw

    def get_angles(self):
        return [self.roll, self.pitch, self.yaw]


class ArduinoIMU(IMU):
    def __init__(self, port, baudrate=115200):
        self.serial = serial.Serial(port, baudrate)
        self.rpy = [0.0, 0.0, 0.0]

    def update(self):
        if not self.serial.in_waiting:
            return
        try:
            line = self.serial.readline().decode("utf-8").strip()
            if not line:
                return
            line = line.split(",")
            if len(line) != 3:
                return

            self.rpy = list(map(float, line))
        except:
            return

    def get_roll(self):
        return self.rpy[0]

    def get_pitch(self):
        return self.rpy[1]

    def get_yaw(self):
        return self.rpy[2]

    def get_angles(self):
        return self.rpy
