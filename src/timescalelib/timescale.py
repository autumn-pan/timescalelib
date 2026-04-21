class Interval:
  def __init__(self, start: float, end: float):
    self.start = start
    self.end = end

  def __eq__(self, other: Interval) -> bool:
    if not isinstance(other, Interval):
      return NotImplemented
    return self.start == other.start and self.end == other.end

  def __repr__(self):
    return f"Interval({self.start}, {self.end})"
    
class TimeScale():
  def __init__(self, intervals: list, scattered_points: list):
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
    for interval in intervals:
      if interval.start == interval.end:
        self.scattered_points.append(interval.start)

    self.intervals = [interval for interval in intervals if interval.start != interval.end]
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

  def __eq__(self, other: TimeScale) -> bool:
    if not isinstance(other, TimeScale):
      return NotImplemented
    return self.intervals == other.intervals and self.scattered_points == other.scattered_points
    
  
  def grain(self, t: float):
    '''Returns the graininess of TimeScale at t
    
        Args:
          t (float): The time point to check the graininess of.

        Returns:
          float: The graininess of the TimeScale at t, which is the distance to the next point in the TimeScale.
    '''
    for interval in self.intervals:
      if interval.start <= t < interval.end:
        return 0
    
    return self.forward_jump(t) - t
  
  def backwards_grain(self, t: float):
    '''Returns the backward graininess of TimeScale at t
    
        Args:
          t (float): The time point to check the backward graininess of.

        Returns:
          float: The backward graininess of the TimeScale at t, which is the distance to the previous point in the TimeScale.
    '''
    for interval in self.intervals:
      if interval.start < t <= interval.end:
        return 0
    
    return t - self.backward_jump(t)
  
  def forward_jump(self, t: float):
    '''Returns the next point in the TimeScale that is greater than t.
    
        Args:
          t (float): The time point to jump from.

        Returns:
          float: The next point in the TimeScale that is greater than t, or t if there is no such point.
    '''
    left_scattered_points = [point for point in self.scattered_points]

    # Check intervals first
    for interval in self.intervals:
      if interval.start <= t < interval.end:
        return t
      left_scattered_points.append(interval.start)
    
    
    for point in left_scattered_points:
      if point > t:
        return point
    
    return t

  def backward_jump(self, t: float):
    '''Returns the previous point in the TimeScale that is less than t.
    
        Args:
          t (float): The time point to jump from.

        Returns:
          float: The previous point in the TimeScale that is less than t, or t if there is no such point.
    '''
    left_scattered_points = [point for point in self.scattered_points]

    # Check intervals first
    for interval in self.intervals:
      if interval.start < t <= interval.end:
        return t
      left_scattered_points.append(interval.end)
    
    
    for point in sorted(left_scattered_points, reverse=True):
      if point < t:
        return point
    
    return t
  
  def in_timescale(self, t: float):
    '''Returns True if t is in TimeScale, False otherwise.

        Args:
          t (float): The point to validate

        Returns:
          bool: Whether or not t is in TimeSclae
    '''
    if t in self.scattered_points:
      return True
    
    for interval in self.intervals:
      if interval.start <= t <= interval.end:
        return True
      
    return False
  
  def __repr__(self):
    return f"TimeScale(intervals={self.intervals}, scattered_points={self.scattered_points})"