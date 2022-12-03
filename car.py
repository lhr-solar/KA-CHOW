import dynamics
import array
import electronics
import motor
import weather
import datetime
import battery_pack
import battery_module

# model of the solar car
# needs main module to initialize and create race strategy
class Car:
    def __init__(self, capacity, voltageOfaSingeCell): #attributes to initialize once then automatically update
        self.voltageOfaSingeCell = voltageOfaSingeCell
        self.voltageOfaSingeCell = 0
        self.capacity = capacity
        
    def drive(self, speed, time, slope, lattitude, longitude): #parameters required for each tick
        #current provided by array
        weather_conditions = weather.Weather(30,-97,datetime.datetime.now(datetime.timezone.utc))
        arr = Array(weather_conditions, 35)
        arr.get_power()
        ArrayVoltage = self.voltageOfASingleCell*242
        currentFromArray = arr/ArrayVoltage

        #current drawn from electronics
        elec = electronics.Electronics()
        electronics_current = elec.run()

        #current drawn by motor
        mot = motor.Motor(speed, slope)
        motor_current = mot.currentMotor()

        #total_current send to battery (- is discharge, + is charge)
        total_current = currentFromArray - (motor_current + electronics_current)

        #calculate capacity loss and SOC of battery pack
        total_pack_capacity = 400 #parameter needs to be verified
        batteryPack = battery_pack.BatteryPack(self.capacity,total_current)
        batteryPack.updateModuleInternalResistance()
        self.capacity -= batteryPack.LostCapacity(self.time) #is batteryCharge the same thing as capactiy?
        battery_charge = (self.capacity/total_pack_capacity)*100

        #print('Current draw from motor:',motor_current,'A')
        #print('Current provided from array:',currentFromArray,'A')
        #print('Current draw from electronics',electronics_current,'A')
        print('Battery is at',battery_charge,'%')


#main function to test the simulator for one set of inputs
#need main module to run race strategy and set parameters from tack
'''
def main():
    speed = 20 #m/s
    time = 0.05 #sec
    slope = 0
    capacity = 400 #Wh
    voltage = 80 #V
    lattitude = 30
    longitude = -97
    solar_mcqueen = Car(speed,time,slope,capacity,voltage,lattitude, longitude)
    solar_mcqueen.drive()
if __name__=="__main__":
    main()
'''