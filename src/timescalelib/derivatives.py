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

    


