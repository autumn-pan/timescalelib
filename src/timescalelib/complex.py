import cmath
import math

from .timescale import TimeScale
from .timescale import integrals

class Complex:
  def __init__(self, value: complex, mu: float):
    if mu <= 0:
      raise ValueError("Error: mu must be positive!")
    if self.value.real == -1/mu:
      raise ValueError("Error: Real part cannot be -1/mu!")

    self.value = value
    self.mu = mu

  def validate_mu(self, other):
    if not math.isclose(self.mu, other.mu):
      raise ValueError("Error: Cannot perform operations between distinct graininess")
    
    return True
  
  @property
  def real(self):
    return (abs(self.value*self.mu+1)-1)/self.mu
  
  @property
  def imag(self):
    return cmath.phase(self.value * self.mu + 1) / self.mu
  
  @property
  def mag(self):
    return abs(self.value)
  
  def __add__(self, other):
    self.validate_mu(other)

    return self + other + self*other*self.mu
  
  def minus(self):
    return -self.value/(1+self.value*self.mu)
  
  def __sub__(self, other):
    self.validate_mu(other)

    return self.value + other.minus
  

def cylinder(c: Complex):
  return cmath.log(c.value*c.mu + 1)/c.mu

def expc(c: Complex, ts: TimeScale, t0: int=0, t: int=None, h: int=1e-5,):
  return cmath.exp(integrals.delta_integral(ts, lambda t: cylinder(c), t0, t, h))
  