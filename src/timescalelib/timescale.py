from timescalelib.basic.jump import forward_jump
from timescalelib.basic.jump import backward_jump

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __eq__(self, other):
    if not isinstance(other, Interval):
      return NotImplemented
    return self.start == other.start and self.end == other.end

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

    # Clean up scattered points
    self.scattered_points = [point for point in scattered_points if not any(interval.start <= point <= interval.end for interval in intervals)]
    # Remove duplicate scattered points
    self.scattered_points = list(set(self.scattered_points))      
    self.scattered_points.sort()

    # Merge overlapping Intervals
    self.intervals.sort(key=lambda x: x.start)
    merged_intervals = []
    for interval in self.intervals:
      if not merged_intervals or merged_intervals[-1].end < interval.start:
        merged_intervals.append(interval)
      else:
        merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
    self.intervals = merged_intervals
      
  def __eq__(self, other):
    if not isinstance(other, TimeScale):
      return NotImplemented
    return self.intervals == other.intervals and self.scattered_points == other.scattered_points
    
  def __repr__(self):
    return f"TimeScale(intervals={self.intervals}, scattered_points={self.scattered_points})"
    
TimeScale.forward_jump = forward_jump
TimeScale.backward_jump = backward_jump

