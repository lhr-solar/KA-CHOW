import numpy as np
import splines, json

from typing import List
from scipy.integrate import quad

class Track:
  # PARAMS:
  #   trackFile: the name of the track file to be used
  def __init__(self, trackFile, friction=.01) -> None:
    points = []
    with open(trackFile) as f:
      geojson = json.load(f)
      features = geojson["features"]
      for feature in features:
          geometry = feature["geometry"]
          coordinates = geometry["coordinates"]
          properties = feature["properties"]

          points.append([*coordinates, properties["elevation"]])
          self.coords = coordinates


    # Determine aspect ratio for scaling
    minLat, maxLat, minLon, maxLon = 90, -90, 180, -180
    for point in points:
        if point[0] < minLon:
            minLon = point[0]
        if point[0] > maxLon:
            maxLon = point[0]
        if point[1] < minLat:
            minLat = point[1]
        if point[1] > maxLat:
            maxLat = point[1]
    aspectRatio = (maxLat - minLat)/(maxLon - minLon)

    # Scale points and convert to km
    for point in points:
        point[0] = (point[0] - minLon)/(maxLon - minLon)
        point[1] = (point[1] - minLat)/(maxLat - minLat)
    points = np.array(points)
    points[:,1] = points[:,1]*aspectRatio
    points = points*.65 #rough conversion to km from lat/lon
    # ^- conversion not accurate, maybe an issue the points. Should be .4 multiple, but the track would too short then

    self.points = points
    cmr = splines.CatmullRom(points, endconditions="closed")
    self.trackLength = self.__arcLength(cmr, 0, len(points)) # in km?
    self.cmr = splines.ConstantSpeedAdapter(cmr) 
    self.tLen = self.cmr.grid[-1]

  # PARAMS
  # y1 = y'(x)
  # y2 = y''(x)
  def __curvature(self, y1: float, y2: float) -> float:
      return (np.abs(y2))/((1+y1**2)**(3/2))

  # Returns R at t in the 2d plane
  def curvature(self, t: float) -> float:
    y1 = self.track.evaluate(t, 1)[1]
    y2 = self.track.evaluate(t, 2)[1]
    return self.__curvature(y1, y2)

  # Returns the slope of the elevation profile at t
  def elevationSlope(self, t: float) -> float:
    return self.cmr.curve.evaluate(np.fmod(t, self.tLen), 1)[2]

  def distanceToT(self, d: float) -> float:
    return d / self.trackLength

  def __arcLength(self, spline, t1, t2) -> float:
    def f(x):
      x1, y1, z1 = spline.evaluate(x, 1)
      return np.sqrt(x1**2 + y1**2)
    return quad(f, t1, t2)[0]

  # max speed at T according to friction
  # math.sqrt(self.GRAVITY * self.mass * self.tire_fricts * radius)
  def maxSpeed(self, t: float, m: float, radius: float) -> float:
    return np.sqrt(9.8, * m * self.friction * radius)
      

if __name__ == "__main__":
    t = Track("track2.json")
    cmr = t.cmr
    print(t.trackLength)