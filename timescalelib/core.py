import array
import numpy as np

from utils.stat import StatMixin
from utils.simplify import SimplifyMixin
from utils.set import SetUtilsMixin

from operators.jumps import JumpOperatorsMixin
from operators.graininess import GraininessMixin
from operators.derivatives import DerivativesMixin

from integrals.integrals import IntegralsMixin

class interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __repr__(self):
    return f"interval({self.start}, {self.end})"
  
    

class TimeScale(
  ExtremumMixin, 
  SimplifyMixin, 
  JumpOperatorsMixin, 
  GraininessMixin,
  DerivativesMixin,
  SetUtilsMixin
): 
  # The timescale is by definition, a union of intervals and scattered points.
  def __init__(self, intervals, scattered_points):
    self.intervals = intervals
    self.scattered_points = scattered_points
    self.simplify()
    
  def __repr__(self):
    return f"timescale(intervals={self.intervals}, scattered_points={self.scattered_points})"
  
  def print_ordered_timescale(self):
    ordered = self.order()
    for item in ordered:
      print(item)