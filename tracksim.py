# simple simulation of the newDynamics class using the track class from the track.py file

from track.track import Track
from newDynamics import newDynamics
import matplotlib.pyplot as plt

def runSim():
    tr = Track("Heartland")

    # mass = 100 kg, tire friction coefficient = 0.01, drag coefficient = 0.5, velocity = 0 m/s, frontal area = 1 m^2
    car = newDynamics(100, 0.01, 0.01, 0.5, 0, 1)

    velocity_list = []
    time_list = []

    currState = tr.getCurr()
    print(currState)

    # for state in range(len(tr.track["features"])):
    #     newState = tr.getNext(currState)
    #     print(newState)
    #     currState = tr.goNext()

    while tr.getNext(tr.getCurr()) != "S0":
        print(tr.getCurr())
        tr.goNext()
        
        




    

if __name__ == "__main__":
    runSim()

    