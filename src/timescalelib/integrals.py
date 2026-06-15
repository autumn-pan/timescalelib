from .timescale import TimeScale
from .timescale import Interval

def delta_integral(ts: TimeScale, f: callable, a: float, b: float, h: int=1e-5):
    '''Returns the delta integral of f from a to b on the timescale ts.

      Args:
        ts (TimeScale): The TimeScale on which to compute the delta integral
        f (callable): The function for which to compute the delta integral
        a (float): The lower bound of integration
        b (float): The upper bound of integration
        h (int, optional): The stepsize in integration over continuous intervals, if the graininess is 0. Defaults to 1e-5
    '''

    if a > b:
      raise ValueError("a must be less than or equal to b")
    if h <= 0:
      raise ValueError("h must be positive")
    
    sum = 0
    
    for i in range(len(ts.scattered_points)):
      if a <= ts.scattered_points[i] <= b:
        if ts.forward_jump(ts.scattered_points[i]) > b:
          break

        sum += f(ts.scattered_points[i]) * ts.grain(ts.scattered_points[i])

    for interval in ts.intervals:
      if interval.end < a:
        continue
      if interval.start > b:
        break

      start = max(interval.start, a)
      end = min(interval.end, b)

      current = start
      while current <= end:
        sum += f(current) * h
        current += h

    return sum
    
def nabla_integral(ts: TimeScale, f: callable, a: float, b: float, h: int=1e-5):
    '''Returns the nabla integral of f from a to b on the timescale ts.

      Args:
        ts (TimeScale): The TimeScale on which to compute the nabla integral
        f (callable): The function for which to compute the nabla integral
        a (float): The lower bound of integration
        b (float): The upper bound of integration
        h (int, optional): The stepsize in integration over continuous intervals, if the graininess is 0. Defaults to 1e-5
    '''

    if a > b:
      raise ValueError("a must be less than or equal to b")
    if h <= 0:
      raise ValueError("h must be positive")
    
    sum = 0
    for i in range(len(ts.scattered_points)):
      if a <= ts.scattered_points[i] <= b:
        if ts.backward_jump(ts.scattered_points[i]) < a:
          continue

        sum += f(ts.scattered_points[i]) * ts.backward_grain(ts.scattered_points[i])

    for interval in ts.intervals:
      if interval.end < a:
        continue
      if interval.start > b:
        break

      start = max(interval.start, a)
      end = min(interval.end, b)

      current = start
      while current <= end:
        sum += f(current) * h
        current += h

    return sum

    
