# timescalelib
`timescalelib` is a user-experience focused Python library that aims to provide a simplified way of performing time-scale calculus. This library is in no way complete, and is an active Work-in-Progress.

## Documentation
### Creating a Time-Scale
A time-scale can be constructed using a set of intervals and points. For example,
```py
  intervals = [Timescale.Interval(0, 1), Timescale.Interval(2, 3)]
  scattered_points = [1.5]
  t = Timescale(intervals, scattered_points)
```
generates a time-scale with two intervals and a point between them. A time-scale can consist of intervals, scattered points, or a mix of both, and consists of the union between the two sets.
#### Generating a Time-Scale
This library also provides a number of tools to automatically generate time-scales based on formulas. This is done so through the `TimeScaleGeneratorClass`, which is initialized using
```py
TimeScaleGenerator()
```
Integer time-scales can be generated with the `TimeScaleGenerator.integer_timescale(self, lower_bound, upper_bound)` method, which returns a time-scale with the set of all integers between the lower and upper bound. The more generalized function `TimeScaleGenerator.arithmetic_timescale(self, lower_bound, upper_bound, step_size)` allows for the construction of time-scales based off arithmetic sequences, with the initial value being `lower_bound`, and in increments of `step_size` up until `upper_bound`.

Geometric sequences can be encoded into time-scales using the `TimeScaleGenerator.geometric_timescale(self, lower_bound, upper_bound, ratio)` method, with the initial value being `lower_bound` and the geometric ratio being `ratio`. 

`TimeScaleGenerator.quantum_timescale(self, lower_bound, upper_bound, base)` generates a time-scale with scattered points of the form `b^n`, where `n` is a natural, and `b != 0`.
### Set Operations with Time-Scales
`TimeScale.element_of(self, t)` determines whether or not a number `t` is an element of the the corresponding time-scale

`TimeScale.append_point(self, t)` returns the union of the time-scale and `t`

`TimeScale.subset(self, other)` determines if `self` is a subset of `other`, for `other` is also a time-scale

`TimeScale.union(self, other)` finds the union between the two time-scales

