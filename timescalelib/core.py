import array
import numpy as np

class interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __repr__(self):
    return f"interval({self.start}, {self.end})"
    

class timescale: 
  # The timescale is by definition, a union of intervals and scattered points.
  def __init__(self, intervals, scattered_points):
    self.intervals = intervals
    self.scattered_points = scattered_points
    self.simplify()
    
  def simplify(self):
    # This method will simplify the timescale by merging overlapping intervals and removing scattered points that are within intervals
    # First, we sort intervals by their starting point
    self.intervals.sort(key=lambda x: x.start)
    # We will use a new list to store the simplified intervals
    simplified_intervals = []
    current_interval = self.intervals[0]
    for interval in self.intervals[1:]:
      if interval.start <= current_interval.end: # If the intervals overlap, then we merge them
        current_interval.end = max(current_interval.end, interval.end)
      else:
        simplified_intervals.append(current_interval)
        current_interval = interval 
    simplified_intervals.append(current_interval) # Don't forget to add the last interval
    self.intervals = simplified_intervals

    # Next, we sort the scattered points
    self.scattered_points.sort()
    # Then, we remove duplicates from the scattered points
    self.scattered_points = list(set(self.scattered_points))
    # Finally, we remove scattered points that are within intervals
    self.scattered_points = [point for point in self.scattered_points if not any(interval.start <= point <= interval.end for interval in self.intervals)]
  
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

  def __repr__(self):
    return f"timescale(intervals={self.intervals}, scattered_points={self.scattered_points})"
  