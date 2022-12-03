import dynamics
import aaron_array
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
        self.capacity = capacity
        
    def drive(self, speed, time, slope, lattitude, longitude): #parameters required for each tick
        #current provided by array
        weather_conditions = weather.Weather(lattitude,longitude,datetime.datetime.now(datetime.timezone.utc))
        arr = aaron_array.Array(weather_conditions, 35)
        ArrayVoltage = self.voltageOfaSingeCell*242
        currentFromArray = arr.get_power()/ArrayVoltage

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
        self.capacity -= batteryPack.LostCapacity(time) #is batteryCharge the same thing as capactiy?
        battery_charge = (self.capacity/total_pack_capacity)*100

        #print('Current draw from motor:',motor_current,'A')
        #print('Current provided from array:',currentFromArray,'A')
        #print('Current draw from electronics',electronics_current,'A')
        print('Battery is at {0:.2f}%'.format(battery_charge))


#main function to test the simulator for one set of inputs
#need main module to run race strategy and set parameters from tack
def main():
    speed = 1 #m/s
    time = 0.05 #hr
    slope = 0
    capacity = 400 #Wh
    voltage = 80 #V
    lattitude = 30
    longitude = -97
    solar_mcqueen = Car(capacity,voltage)
    solar_mcqueen.drive(speed,time,slope,lattitude, longitude)
if __name__=="__main__":
    main()