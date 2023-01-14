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
        
    def drive(self, speed, time, slope, latitude, longitude): #parameters required for each tick
        #current provided by array
        arr = aaron_array.Array(self.weather_conditions, 35)
        ArrayVoltage = self.voltageOfaSingeCell*242
        #currentFromArray = arr.get_power()/ArrayVoltage
        array_power = arr.get_power()

        #current drawn from electronics
        elec = electronics.Electronics()
        electronics_power = elec.run()

        #current drawn by motor
        mot = motor.Motor(speed, slope)
        motor_current = mot.currentMotor()
        motor_power = motor_current*96
        max_speed = mot.dynamics.max_velocity(abs(slope))

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
    capacity = 5400 #Wh of individual cell
    voltage = 3.7 #V
    
    startingTime = datetime.datetime(2023, 1, 10, 0, 0, 0).timestamp()
    currTime = startingTime
    currDis = 0

    t = track.Track("trackDynamic")
    t.setForks("left", "left", "left")
    lat, lon = t.getCoords()
    solar_mcqueen = Car(capacity, voltage, lat, lon, startingTime)


    while t.getNext(t.getCurr()) != "S0":
        totalDistance = t.getDistance(t.getCurr(), t.getNext(t.getCurr()))
        lat, lon = t.getCoords()
        print(speed, currTime, t.getSlopeRadians(), lat, lon)
        targetSpeed = solar_mcqueen.drive(speed, currTime, t.getSlopeRadians(), lat, lon)
        print(f'Fastest speed: {targetSpeed}')

        currDis += speed*180
        print(f'Progress: {currDis/totalDistance}')
        print(f'currTime: {currTime - startingTime}')
        if currDis >= totalDistance:
            t.goNext()
            currDis = currDis - totalDistance
        time.sleep(.5)
        currTime += 180

if __name__=="__main__":
    main()
    