# timescalelib/operators/jumps.py


class JumpOperatorsMixin:
  def right_dense_points(self):
    # Returns a list of all scattered points as well as the right endpoints of all intervals
    right_dense = [interval.end for interval in self.intervals] + self.scattered_points
    right_dense.sort()
    return right_dense

  def forward_jump(self, t):
    # The forward jump of t in ts is the smallest point in the timescale that is greater than t
    # If t is the upper bound of the timescale, then it is its own forward jump
    if t == self.max():
      return t
    
    # Likewise, if t is within an interval and it is not the upper bound of the interval, then its forward jump is itself
    for interval in self.intervals:
      if interval.start <= t < interval.end:
        return t
      
    # Otherwise, we need to find the smallest point in the timescale that is greater than t
    candidates = [interval.start for interval in self.intervals if interval.start > t] + [point for point in self.scattered_points if point > t]
    return min(candidates)
  
  def backward_jump(self, t):
    # The backward jump of t in ts is the largest point in the timescale that is less than t
    # If t is the lower bound of the timescale, then it is its own backward jump
    if t == self.min():
      return t
    
    # Likewise, if t is within an interval and it is not the lower bound of the interval, then its backward jump is itself
    for interval in self.intervals:
      if interval.start < t <= interval.end:
        return t
      
    # Otherwise, we need to find the largest point in the timescale that is less than t
    candidates = [interval.end for interval in self.intervals if interval.end < t] + [point for point in self.scattered_points if point < t]
    return max(candidates)