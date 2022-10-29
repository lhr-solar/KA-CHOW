import array
import battery_pack
import dynamics
import electronics
import motor
# model of the solar car

class Car:
    # TODO: put a bunch of stuff in here
    def __init__(self):
        self.SOC = 0
        self.speed = 0
    # TODO: maybe change the parameters to make this make more sense
    def drive(self, speed, time):
        # simulate mechanical losses

        # simulate electronics, array, and motor losses to figure out current provided/requested

        # simulate battery losses/gains

        # provide CAN outputs
        print("something")