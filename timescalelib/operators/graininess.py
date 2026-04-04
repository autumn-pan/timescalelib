# operators/graininess.py

class GraininessMixin:
  def graininess(self, t):
    # The graininess of t in ts is the distance between t and its forward jump
    return self.forward_jump(t) - t
  
  def backward_graininess(self, t):
    # The backward graininess of t in ts is the distance between t and its backward jump
    return t - self.backward_jump(t)