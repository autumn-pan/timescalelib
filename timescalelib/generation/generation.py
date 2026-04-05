# timescalelib/generation/generation.py

from timescalelib.core import TimeScale

class TimeScaleGenerator:
  def __init__(self):
    pass

  def scattered_timescale(self, lower_bound, upper_bound, formula, step_size):
    # Generates a timescale from lower_bound to upper_bound where the points in the timescale are a sequence defined by the formula and the step size
    intervals = []
    scattered_points = []
    t = lower_bound
    while t <= upper_bound:
      if formula(t):
        scattered_points.append(t)
      t += step_size
    return TimeScale(intervals, scattered_points)
  
  def hybrid_timescale(self, lower_bound, upper_bound, formula, step_size, intervals):
    # Generates a timescale from lower_bound to upper_bound where the points in the timescale are defined by the formula and the step size, but also includes intervals where the formula is true for all points in the interval
    scattered_points = self.scattered_timescale(lower_bound, upper_bound, formula, step_size).scattered_points
    return TimeScale(intervals, scattered_points)
  
  def integer_timescale(self, lower_bound, upper_bound):
    # Generates a timescale from lower_bound to upper_bound where the points in the timescale are all integers between lower_bound and upper_bound
    intervals = []
    scattered_points = [t for t in range(lower_bound, upper_bound + 1)]
    return TimeScale(intervals, scattered_points)
  
  def arithmetic_timescale(self, lower_bound, upper_bound, step_size):
    # Generates a timescale from lower_bound to upper_bound where the points in the timescale are all points of the form lower_bound + n * step_size for n an integer such that lower_bound + n * step_size <= upper_bound
    if step_size == 0:
      raise ValueError("Step size cannot be zero.")
    
    intervals = []
    scattered_points = []
    t = lower_bound
    while t <= upper_bound:
      scattered_points.append(t)
      t += step_size
    return TimeScale(intervals, scattered_points)
  
  def geometric_timescale(self, lower_bound, upper_bound, ratio):
    # Generates a timescale from lower_bound to upper_bound where the points in the timescale are all points of the form lower_bound * ratio^n for n an integer such that lower_bound * ratio^n <= upper_bound
    if ratio == 0:
      raise ValueError("Ratio cannot be zero.")
    
    intervals = []
    scattered_points = []
    t = lower_bound
    while t <= upper_bound:
      scattered_points.append(t)
      t *= ratio
    return TimeScale(intervals, scattered_points)
  
  def quantum_timescale(self, lower_bound, upper_bound, base):
    # Generates a timescale from lower_bound to upper_bound where the points in the timescale are all points of the form base^n for n an integer such that base^n >= lower_bound and base^n <= upper_bound
    if base == 0:
      raise ValueError("Base cannot be zero.")
    
    intervals = []
    scattered_points = []
    n = 0
    t = base ** n
    while t <= upper_bound:
      if t >= lower_bound:
        scattered_points.append(t)
      n += 1
      t = base ** n
    return TimeScale(intervals, scattered_points)