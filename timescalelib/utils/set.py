# timescalelib/utils/set.py

from timescalelib.core import TimeScale

class SetUtilsMixin:
  def is_subset(self, other):
    # Returns true if self is a subset of other, false otherwise
    for interval in self.intervals:
      if not any(other_interval.start <= interval.start and interval.end <= other_interval.end for other_interval in other.intervals):
        return False
    for point in self.scattered_points:
      if point not in other.scattered_points and not any(other_interval.start <= point <= other_interval.end for other_interval in other.intervals):
        return False
    return True
  
  def union(self, other):
    # Returns the union of self and other as a new timescale
    new_intervals = self.intervals + other.intervals
    new_scattered_points = self.scattered_points + other.scattered_points
    return TimeScale(new_intervals, new_scattered_points) 
  
  def intersection(self, other):
    # Returns the intersection of self and other as a new timescale
    new_intervals = []
    for interval in self.intervals:
      for other_interval in other.intervals:
        start = max(interval.start, other_interval.start)
        end = min(interval.end, other_interval.end)
        if start < end:
          new_intervals.append(interval(start, end))
    new_scattered_points = [point for point in self.scattered_points if not point in other.scattered_points and any(other_interval.start <= point <= other_interval.end for other_interval in other.intervals)]
    return TimeScale(new_intervals, new_scattered_points)
  
  def element_of(self, t):
    # Returns true if t is an element of self, false otherwise
    if t in self.scattered_points:
      return True
    for interval in self.intervals:
      if interval.start <= t <= interval.end:
        return True
    return False
  
  def append_point(self, t):
    # Appends a point to the timescale, if it is not already an element of the timescale
    self.scattered_points.append(t)
    self.simplify()

  def IntervalOfPoint(self, t):
    # Returns the interval that contains t, if it exists, None otherwise
    for interval in self.intervals:
      if interval.start <= t <= interval.end:
        return interval
    return None