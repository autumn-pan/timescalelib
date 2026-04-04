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

  
  def __repr__(self):
    return f"timescale(intervals={self.intervals}, scattered_points={self.scattered_points})"
  