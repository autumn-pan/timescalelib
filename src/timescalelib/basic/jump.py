class JumpMixin:
  '''Mixin class that provides jump functionality for TimeScale.'''
    
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