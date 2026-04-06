# timescalelib/utils/extremum.py

class StatMixin:
  def max(self):
    # The maximum of the timescale is the maximum of the end points of the intervals and the maximum of the scattered points
    max_interval = max(interval.end for interval in self.intervals) if self.intervals else float('-inf')
    max_scattered = max(self.scattered_points) if self.scattered_points else float('-inf')
    return max(max_interval, max_scattered)
  
  def min(self):
    # The minimum of the timescale is the minimum of the start points of the intervals and the minimum of the scattered points
    min_interval = min(interval.start for interval in self.intervals) if self.intervals else float('inf')
    min_scattered = min(self.scattered_points) if self.scattered_points else float('inf')
    return min(min_interval, min_scattered)
  
  def range(self):
    # The range of the timescale is the interval from the minimum to the maximum
    return (self.min(), self.max())
  