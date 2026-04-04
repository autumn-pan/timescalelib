import array
import numpy as np

from utils.extremum import ExtremumMixin
from utils.simplify import SimplifyMixin
from operators.jumps import JumpOperatorsMixin
from operators.graininess import GraininessMixin

class interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __repr__(self):
    return f"interval({self.start}, {self.end})"
    

class timescale(
  ExtremumMixin, 
  SimplifyMixin, 
  JumpOperatorsMixin, 
  GraininessMixin
): 
  # The timescale is by definition, a union of intervals and scattered points.
  def __init__(self, intervals, scattered_points):
    self.intervals = intervals
    self.scattered_points = scattered_points
    self.simplify()
    
  def __repr__(self):
    return f"timescale(intervals={self.intervals}, scattered_points={self.scattered_points})"
  