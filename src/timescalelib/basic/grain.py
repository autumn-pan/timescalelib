

class GrainMixin:
  """Mixin for graininess over time-scales"""

  def grain(self, t: float):
    '''Returns the graininess of TimeScale at t
    
        Args:
          t (float): The time point to check the graininess of.

        Returns:
          float: The graininess of the TimeScale at t, which is the distance to the next point in the TimeScale.
    '''
    for interval in self.intervals:
      if interval.start <= t < interval.end:
        return 0
    
    return self.forward_jump(t) - t
  
  def backwards_grain(self, t: float):
    '''Returns the backward graininess of TimeScale at t
    
        Args:
          t (float): The time point to check the backward graininess of.

        Returns:
          float: The backward graininess of the TimeScale at t, which is the distance to the previous point in the TimeScale.
    '''
    for interval in self.intervals:
      if interval.start < t <= interval.end:
        return 0
    
    return t - self.backward_jump(t)