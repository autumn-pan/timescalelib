import math

from .timescale import TimeScale
from .timescale import Interval

def delta_derivative(ts: TimeScale, f: callable, t: float, h: float = 1e-5):
    '''Returns the delta derivative of f at t on the timescale ts.

      Args:
        ts (TimeScale): The TimeScale on which to compute the delta derivative
        f (callable): The function for which to compute the delta derivative
        t (float): The point at which to compute the delta derivative
        h (float, optional): The step size to use for numerical approximation, if the graininess is 0. Defaults to 1e-5

      Returns: 
        float: The delta derivative of f at t on the timescale ts
    '''

    if not ts.__contains__(t):
      raise ValueError(f"t={t} is not in the timescale")
    
    if t == ts.supremum():
      raise ValueError(f"t={t} is the supremum of the timescale, so the delta derivative is not defined")
    
    if h <= 0:
      raise ValueError("h must be positive")

    if ts.forward_jump(t) == t:
      return (f(t + h) - f(t)) / h
    
    return (f(ts.forward_jump(t)) - f(t)) / ts.grain(t)

def nabla(ts: TimeScale, f: callable, t: float, h: float = 1e-5):
    '''Returns the delta derivative of f at t on the timescale ts.

      Args:
        ts (TimeScale): The TimeScale on which to compute the delta derivative
        f (callable): The function for which to compute the delta derivative
        t (float): The point at which to compute the delta derivative
        h (float, optional): The step size to use for numerical approximation, if the graininess is 0. Defaults to 1e-5

      Returns: 
        float: The nabla derivative of f at t on the timescale ts
    '''

    if not ts.__contains__(t):
      raise ValueError(f"t={t} is not in the timescale")
    
    if t == ts.supremum():
      raise ValueError(f"t={t} is the supremum of the timescale, so the delta derivative is not defined")
    
    if h <= 0:
      raise ValueError("h must be positive")

    if ts.backward_jump(t) == t:
      return (f(t + h) - f(t)) / h
    
    return (f(ts.backward_jump(t)) - f(t)) / ts.backward_grain(t)

