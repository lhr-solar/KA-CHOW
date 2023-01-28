import datetime, time, math

from car import Car
from track import Track

trackFile = "track2.json"

track = Track(trackFile)

tickLength = 5 #seconds per tick

class Day:
  def __init__(self, startTime: int, runTime: int) -> None:
    self.startTime = startTime
    self.runTime = runTime
 
nineHours = 60*60*9
days = [Day(datetime.datetime(2023, 1, 10 + i, 9, 0, 0).timestamp(), nineHours) for i  in range(3)]

for i, day in enumerate(days):
  currentTime = day.startTime
  print(f"\n-------DAY {i+1} STARTING AT {datetime.datetime.fromtimestamp(day.startTime)}-------")
  car = Car(track, day.startTime)
  currDist = 0
  while currentTime < day.startTime + day.runTime:
    print("Time Passed:", currentTime - day.startTime)
    slope = track.elevationSlope(track.distanceToT(currDist))/180 * math.pi
    print(f'Slope: {slope}')
    currDist += car.drive(10, slope, currentTime)
    # car will drive off max lol
    currentTime += tickLength
    time.sleep(0.2)
    print()