class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __repr__(self):
    return f"Interval({self.start}, {self.end})"
    
class TimeScale:
  def __init__(self, intervals, scattered_points):
    '''Initialize the TimeScale with a list of intervals and scattered points.
    
        Args:
          intervals (list of Interval): A list of Interval objects representing the time intervals.
          scattered_points (list of int): A list of integers representing the scattered points in time.

        The constructor processes the intervals and scattered points to ensure that:
          1. No duplicate scattered points are present.
          2. Any overlapping intervals are merged
          3. Any interval that reduces to a single point (where start == end) is converted to a scattered point and removed from the intervals list.
          4. Any scattered point that falls within an interval is removed from the scattered points list, as it is already covered by the interval.
    '''
    self.intervals = intervals
    scattered_points = set(scattered_points)
    for interval in intervals:
      for point in scattered_points:
        if interval.start <= point <= interval.end:
          scattered_points.remove(point)
    
    # Merge overlapping intervals
    self.intervals.sort(key=lambda x: x.start)
    merged_intervals = []
    current_interval = self.intervals[0]
    for next_interval in self.intervals[1:]:
      if current_interval.end >= next_interval.start:
        current_interval.end = max(current_interval.end, next_interval.end)
      else:
        merged_intervals.append(current_interval)
        current_interval = next_interval
      merged_intervals.append(current_interval)

    for interval in merged_intervals:
      if interval.start == interval.end:
        scattered_points.append(interval.start)
        merged_intervals.remove(interval)

    self.intervals = merged_intervals
    self.scattered_points = sorted(scattered_points)
      
    def __repr__(self):
        return f"TimeScale({self.intervals})"
    
from .basic.jump import forward_jump
TimeScale.forward_jump = forward_jump