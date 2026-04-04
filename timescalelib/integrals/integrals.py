# timescalelib/operators/integrals.py

class IntegralsMixin:
  def integrate_interval(self, f, interval, fallback_stepsize=1e-5):
    # The delta integral of f over the interval, where the step size is fallback_stepsize
    sum = 0
    for t in self.generate_points(interval.start, interval.end, fallback_stepsize):
      sum += f(t) * fallback_stepsize
    return sum
  
  def delta_integral(self, f, lower_bound, upper_bound, fallback_stepsize=1e-5):
    # The integral of f from lower_bound to upper_bound, where the step size is defined by the forward graininess
    
    sum = 0
    candidate_intervals = {interval for interval in self.intervals if interval.start >= lower_bound and interval.end <= upper_bound}
    candidate_right_scattered_points = (point for point in self.right_dense_points() if point >= lower_bound and point <= upper_bound)

    # Add the integrals over continuous intervals
    for interval in candidate_intervals:
      sum += self.integrate_interval(f, interval, fallback_stepsize)

    # Add the sums over right-scattered points
    for point in candidate_right_scattered_points:
      sum += f(point) * self.graininess(point)

    return sum
  
  def nabla_integral(self, f, lower_bound, upper_bound, fallback_stepsize=1e-5):
    # The nabla integral of f from lower_bound to upper_bound, where the step size is defined by the backward graininess
    
    sum = 0
    candidate_intervals = {interval for interval in self.intervals if interval.start >= lower_bound and interval.end <= upper_bound}
    candidate_left_scattered_points = (point for point in self.left_scattered_points() if point >= lower_bound and point <= upper_bound)

    # Add the integrals over continuous intervals
    for interval in candidate_intervals:
      sum += self.integrate_interval(f, interval, fallback_stepsize)

    # Add the sums over left-scattered points
    for point in candidate_left_scattered_points:
      sum += f(point) * self.backward_graininess(point)

    return sum

