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
    self.scattered_points = scattered_points
      
    def __eq__(self, other):
      if not isinstance(other, TimeScale):
        return NotImplemented
      return self.intervals == other.intervals and self.scattered_points == other.scattered_points
    
    def __repr__(self):
        return f"TimeScale({self.intervals})"
    
from .basic.jump import forward_jump, backward_jump
TimeScale.forward_jump = forward_jump
TimeScale.backward_jump = backward_jump

