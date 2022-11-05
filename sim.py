# test the newDynamics class with a simple square track.

# import the newDynamics class
from newDynamics import newDynamics
import matplotlib.pyplot as plt

# create a new instance of the newDynamics class
# mass = 100 kg, tire friction coefficient = 0.01, drag coefficient = 0.5, velocity = 0 m/s, frontal area = 1 m^2
newDynamics = newDynamics(100, 0.01, 0.5, 0, 1)

def create_square_track():
    # create a square track
    # the first side of the square will be 100 meters long, with a 10% slope, vehicle will accelerate to 10 m/s
    # the second side of the square will be 100 meters long, with a 0% slope, vehicle will decelerate to 5 m/s
    # the third side of the square will be 100 meters long, with a -10% slope, vehicle will decelerate to 2.5 m/s
    # the fourth side of the square will be 100 meters long, with a 0% slope, vehicle will accelerate to 5 m/s
    square_track = [[100, 10, 10], [100, 0, 5], [100, -10, 2.5], [100, 0, 5]]
    return square_track

def plot_square_track():
    # plot the vehicle dynamics on the square track
    square_track = create_square_track()

    # create lists to store the data
    time_list = []
    velocity_list = []
    acceleration_list = []

    for side in square_track:
        # calculate the time required to complete the current side of the square
        time = side[0] / side[2]
        # update the time of the vehicle
        newDynamics.update_time(time)
        # update the velocity of the vehicle
        newDynamics.update_velocity(side[2])
        # check if velocity is correct
        assert newDynamics.get_velocity == side[2]
        # calculate the total propelling force required to complete the current side of the square
        total_propelling_force = newDynamics.total_propelling_force(side[1])
        # print the results
        print("The total propelling force required to complete the current side of the square is " + str(total_propelling_force) + " N.")
        print("The time required to complete the current side of the square is " + str(time) + " s.")
        print("The velocity of the vehicle at the end of the current side of the square is " + str(side[2]) + " m/s.")
        print("The acceleration of the vehicle at the end of the current side of the square is " + str((side[2] - newDynamics.old_velocity) / time) + " m/s^2.")
        print()
        # add the data to the lists
        time_list.append(time)
        velocity_list.append(side[2])
        acceleration_list.append((side[2] - newDynamics.old_velocity) / time)

    # plot the data with labels
    plt.plot(time_list, velocity_list, label = "Velocity")
    plt.plot(time_list, acceleration_list, label = "Acceleration")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s) and Acceleration (m/s^2)")
    plt.title("Vehicle Dynamics on a Square Track")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_square_track()