class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __repr__(self):
    return f"Interval({self.start}, {self.end})"
    
class TimeScale:
  def __init__(self, intervals, scattered_points):
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

    self.intervals = merged_intervals
    self.scattered_points = sorted(scattered_points)
      
    def __repr__(self):
        return f"TimeScale({self.intervals})"
    
