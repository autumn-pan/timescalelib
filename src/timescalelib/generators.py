from .timescale import TimeScale
from .timescale import Interval

def generate_alternating(a,b, t, t0=0):
  points = []
  current = t0
  while current <= t:
    points.append(current)
    current += a
    if current > t:
      break
    points.append(current)
    current += b

  return TimeScale([], points)

def generate_by_graininess(a, t, t0):
  for i in a:
    if i <= 0:
      raise ValueError("Error: All graininess values must be positive!")
  points = []
  current = t0
  while current <= t:
    points.append(current)
    current += a[len(points) % len(a)]

  return TimeScale([], points)

def generate_discrete(h, t, t0):
  points = []
  current = t0
  while current <= t:
    points.append(current)
    current += h
  return TimeScale([], points)

def generate_disjoint_intervals(a, b, t, t0):
  if a <= 0 or b <= 0:
    raise ValueError("Error: a and b must be positive!")
  
  intervals = []
  current = t0
  while current <= t:
    intervals.append(Interval(current, current + a))
    current += a + b

  return TimeScale(intervals, [])