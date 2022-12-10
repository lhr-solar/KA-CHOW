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
    def __init__(self, capacity, voltageOfaSingeCell): #attributes to initialize once then automatically update
        self.voltageOfaSingeCell = voltageOfaSingeCell
        self.capacity = capacity
        
    def drive(self, speed, time, slope, latitude, longitude): #parameters required for each tick
        #current provided by array
        weather_conditions = weather.Weather(latitude,longitude,datetime.datetime.now())
        arr = aaron_array.Array(weather_conditions, 35)
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
        
        return speed


#main function to test the simulator for one set of inputs
#need main module to run race strategy and set parameters from tack
def main():
    newSpeed = 2 #m/s
    capacity = 5400 #Wh of individual cell
    voltage = 3.7 #V
    
    t = track.Track("trackDynamic")
    t.setForks("left", "left", "left")
    solar_mcqueen = Car(capacity, voltage)

    while t.getNext(t.getCurr()) != "S0":
        print(t.getCurr())
        lat, lon = t.getCoords()
        print(newSpeed, t.getDistance()/(3600*newSpeed), t.getSlopeRadians(), lat, lon)
        newSpeed = solar_mcqueen.drive(newSpeed, t.getDistance()/(3600*newSpeed), t.getSlopeRadians(), lat, lon)
        t.goNext()
        time.sleep(.5)

if __name__=="__main__":
    main()
    