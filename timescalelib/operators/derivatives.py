# timescalelib/operators/derivatives.py

class DerivativesMixin:
  def delta_derivative(self, f, t, fallback_stepsize=1e-5):
    # The derivative of f at t, where the step size is defined by the forward graininess
    
    graininess = self.graininess(t)
    if graininess == 0:
      # If the graininess is zero, we can use the fallback step size so that we don't get a division by zero error
      graininess = fallback_stepsize

    return (f(t + graininess) - f(t)) / graininess
  
  def nabla_derivative(self, f, t, fallback_stepsize=1e-5):
    # The nabla derivative of f at t, where the step size is defined by the backward graininess
    
    backward_graininess = self.backward_graininess(t)
    if backward_graininess == 0:
      # If the backward graininess is zero, we can use the fallback step size so that we don't get a division by zero error
      backward_graininess = fallback_stepsize

    return (f(t) - f(t - backward_graininess)) / backward_graininess
    
