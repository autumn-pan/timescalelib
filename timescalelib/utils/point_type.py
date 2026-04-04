# timescalelib/utils/point_type.py

class PointTypeMixin:
  def point_type(self, t):
    # Returns "right-dense" if t is a right-dense point, "left-dense" if t is a left-dense point, "isolated" if t is an isolated point, and "undefined" if t is not an element of the timescale
    if t in self.scattered_points:
      return "isolated"
    for interval in self.intervals:
      if interval.start <= t <= interval.end:
        if t == interval.start and t == interval.end:
          return "isolated"
        elif t == interval.start:
          return "right-dense"
        elif t == interval.end:
          return "left-dense"
        else:
          return "undefined"
    return "undefined"
  
  def right_scattered_points(self):
    # Returns a list of all right-scattered points, which are the points that are right-dense but not left-dense
    right_scattered = []

    # On simplified time-scales, the end points of intervals are always right-scattered
    for interval in self.intervals:
      right_scattered.append(interval.end)

    # Scattered points are by definition, both right-scattered and left-scattered
    for point in self.scattered_points:
      right_scattered.append(point)
    return right_scattered
  
  def left_scattered_points(self):
    # Returns a list of all left-scattered points, which are the points that are left-dense but not right-dense
    left_scattered = []

    # On simplified time-scales, the start points of intervals are always left-scattered
    for interval in self.intervals:
      left_scattered.append(interval.start)

    # Scattered points are by definition, both right-scattered and left-scattered
    for point in self.scattered_points:
      left_scattered.append(point)
    return left_scattered