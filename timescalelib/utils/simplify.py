# timescalelib/utils/simplify.py

class SimplifyMixin:
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

  def order(self):
    # Returns an ordered list of all points and intervals in the time-scale
    ordered = []
    remaining_points = set(self.scattered_points)
    for interval in self.intervals:
      # Add all points that are less than the start of the interval
      for point in remaining_points:
        if point < interval.start:
          ordered.append(point)
          remaining_points.remove(point)
        else:
          break
      # Add the interval
      ordered.append(interval)

    # Add any remaining points
    for point in remaining_points:
      ordered.append(point)
    return ordered
  