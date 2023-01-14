import dynamics
import aaron_array
import electronics
import motor
import weather
import datetime
import battery_pack
import battery_module
import time
import track
import math

# model of the solar car
# needs main module to initialize and create race strategy
class Car:
    def __init__(self, capacity, voltageOfaSingeCell, latitude, longitude, startingTime): #attributes to initialize once then automatically update
        self.voltageOfaSingeCell = voltageOfaSingeCell
        self.capacity = capacity
        self.weather_conditions = weather.Weather(latitude,longitude, startingTime)
        self.elec = electronics.Electronics()
        self.mot = motor.Motor()
        
    def drive(self, speed, time, slope, latitude, longitude): #parameters required for each tick
        #current provided by array
        self.weather_conditions.pull_weather_data(time)
        arr = aaron_array.Array(self.weather_conditions, 35)
        ArrayVoltage = self.voltageOfaSingeCell*242
        #currentFromArray = arr.get_power()/ArrayVoltage
        array_power = arr.get_power() #THIS IS IN POWER

        #current drawn from electronics
        electronics_power = self.elec.run() #THIS IS IN CURRENT

        #current drawn by motor
        self.mot.updateParameters(speed, slope)
        motor_current = self.mot.currentMotor() #CURRENT
        motor_power = motor_current*96 #?!?!?!?! what is multiplier of 96????
        print(slope)
        max_speed = self.mot.dynamics.max_velocity(abs(slope))

        #total_current send to battery (- is discharge, + is charge)
        total_power = array_power - (motor_power + electronics_power)

        #calculate capacity loss and SOC of battery pack
        total_pack_capacity = 5400 #parameter needs to be verified
        batteryPack = battery_pack.BatteryPack(self.capacity/432,total_power)
        batteryPack.updateModuleInternalResistance()
        self.capacity += batteryPack.LostCapacity(time) #is batteryCharge the same thing as capactiy?
        battery_charge = (self.capacity/total_pack_capacity)*100

        print('Power draw from motor: {0:.2f} W'.format(motor_power))
        print('Power provided from array: {0:.2f} W'.format(array_power))
        print('Power draw from electronics {0:.2f} W'.format(electronics_power))
        print('Battery is at {0:.2f}%'.format(battery_charge))
        
        return max_speed


#main function to test the simulator for one set of inputs
#need main module to run race strategy and set parameters from tack
def main():
    speed = 0 #m/s
    acc = 4 #m/s^2

    capacity = 5400 #Wh of individual cell
    voltage = 3.7 #V
    
    startingTime = datetime.datetime(2023, 1, 10, 0, 0, 0).timestamp()
    currTime = startingTime
    currDis = 0

    t = track.Track("trackDynamic")
    t.setForks("left", "left", "left")
    lat, lon = t.getCoords()
    solar_mcqueen = Car(capacity, voltage, lat, lon, startingTime)

    timeFactor = 30 #seconds per tick

    while t.getNext(t.getCurr()) != "S0":
        totalDistance = t.getDistance(t.getCurr(), t.getNext(t.getCurr()))
        lat, lon = t.getCoords()
        print(speed, currTime, t.getSlopeRadians(), lat, lon)
        targetSpeed = solar_mcqueen.drive(speed, currTime, t.getSlopeRadians(), lat, lon)
        print(f'Fastest speed: {targetSpeed}')

        timeToReach = (targetSpeed - speed)/acc
        if timeToReach > timeFactor:
            dist = speed*timeFactor**2/2 + acc*timeFactor**3/6
            speed += acc*timeFactor
        else:
            dist = speed*timeToReach**2/2 + acc*timeToReach**3/6
            dist += targetSpeed*(timeFactor - timeToReach)
            speed = targetSpeed

        print(f'Speed: {speed}m/s')
        print(f'Traveled: {dist}m')
        currDis += dist

        t.goDistance(currDis)
        print(t.curr)

        print(f'Current distance: {currDis}m')
        print(f'Current time: {currTime - startingTime}')

        time.sleep(1)
        currTime += timeFactor

if __name__=="__main__":
    main()
    