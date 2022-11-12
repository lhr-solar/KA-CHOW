# test the newDynamics class with a simple square track.

# import the newDynamics class
from newDynamics import newDynamics
import matplotlib.pyplot as plt

# create a new instance of the newDynamics class
# mass = 100 kg, tire friction coefficient = 0.01, drag coefficient = 0.5, velocity = 0 m/s, frontal area = 1 m^2
newDynamics = newDynamics(100, 0.01, 0.01, 0.5, 0, 1)


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

    # simulate the vehicle dynamics on the square track by displaying the velocity and acceleration of the vehicle as the vehicle moves along each side of the square track
    for side in square_track:
        distance = 0
        time = 0
        while (distance < side[0]):
            print("side number: ", square_track.index(side) + 1)
            # the track data is stored in a list of lists. Each list contains the length of the side, the slope of the side, and the target velocity of the side
            # to run a simulation, we need to use the newDynamics class to find the force that the vehicle needs to overcome to accelerate to the target velocity
            # once the vehicle has reached the target velocity, keep the vehicle at the target velocity until the vehicle has traveled the length of the side
            if (newDynamics.get_velocity() < side[2]):
                force = newDynamics.total_propelling_force(side[1])
                acceleration = force / newDynamics.mass        
                distance += newDynamics.get_velocity() * time + 0.5 * acceleration * time * time
                velocity = newDynamics.get_velocity() + acceleration * time

            newDynamics.update_time(time)
            newDynamics.update_velocity(velocity)   

# plot the time, velocity, and acceleration of the vehicle on the square track
    plt.plot(time_list, velocity_list, label="Velocity")
    plt.plot(time_list, acceleration_list, label="Acceleration")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s) and Acceleration (m/s^2)")
    plt.legend()
    plt.show()


def old_sim():
    square_track = create_square_track()

    # create lists to store the data
    time_list = []
    velocity_list = []
    acceleration_list = []

    for side in square_track:
        distance = 0
        while (distance < side[0]):
            print("side number: ", square_track.index(side) + 1)
            # the track data is stored in a list of lists. Each list contains the length of the side, the slope of the side, and the target velocity of the side
            # to run a simulation, we need to use the newDynamics class to find the force that the vehicle needs to overcome to accelerate to the target velocity
            force = newDynamics.total_propelling_force(side[1])
            print("Force: " + str(force))
            # we also need to find the time it takes to accelerate to the target velocity
            time = (side[2] - newDynamics.get_velocity()) / (force / newDynamics.mass)
            print("Time: " + str(time))
            # we also need to find the acceleration of the vehicle
            acceleration = force / newDynamics.mass
            print("Acceleration: " + str(acceleration))
            # we also need to find the distance the vehicle will travel in the time it takes to accelerate to the target velocity
            distance += newDynamics.get_velocity() * time + 0.5 * acceleration * time * time
            print("Distance: " + str(distance))
            # we also need to find the velocity of the vehicle at the end of the time it takes to accelerate to the target velocity
            velocity = newDynamics.get_velocity() + acceleration * time
            print("Velocity: " + str(velocity))

            # update the time of the vehicle
            newDynamics.update_time(time)
            # update the velocity of the vehicle
            newDynamics.update_velocity(velocity)

            # add the time, velocity, and acceleration to the lists
            time_list.append(time)
            velocity_list.append(velocity)
            acceleration_list.append(acceleration)

            


if __name__ == "__main__":
    old_sim()
