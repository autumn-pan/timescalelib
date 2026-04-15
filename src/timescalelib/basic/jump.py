def forward_jump(self, t):
  '''Returns the next point in the TimeScale that is greater than t.
  
      Args:
        t (int): The time point to jump from.

      Returns:
        int: The next point in the TimeScale that is greater than t, or t if there is no such point.
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