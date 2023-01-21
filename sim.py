import datetime, time

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
  while currentTime < day.startTime + day.runTime:
    print("Time Passed:", currentTime - day.startTime)
    car.drive(28.8, 0.174533, currentTime)
    currentTime += tickLength
    time.sleep(1)
    print()