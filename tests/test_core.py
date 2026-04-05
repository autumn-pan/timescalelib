def test_construction():
  from timescalelib.core import Timescale

  intervals = [Timescale.Interval(0, 1), Timescale.Interval(2, 3)]
  scattered_points = [1.5, 2.5]
  t = Timescale(intervals, scattered_points)

  assert t.intervals == intervals
  assert t.scattered_points == scattered_points

def test_simplification():
  from timescalelib.core import Timescale

  intervals = [Timescale.Interval(0, 1), Timescale.Interval(0.5, 1.5), Timescale.Interval(2, 3)]
  scattered_points = [1.5, 2.5, 1, 0, 0.5]
  t = Timescale(intervals, scattered_points)

  assert t.intervals == [Timescale.Interval(0, 1.5), Timescale.Interval(2, 3)]
  assert t.scattered_points == [1, 2.5]
def test_empty_timescale():
  from timescalelib.core import Timescale

  t = Timescale([], [])
  assert t.intervals == []
  assert t.scattered_points == []

def test_single_point_timescale():
  from timescalelib.core import Timescale

  t = Timescale([], [1])
  assert t.intervals == []
  assert t.scattered_points == [1]

def test_single_interval_timescale():
  from timescalelib.core import Timescale

  t = Timescale([Timescale.Interval(0, 1)], [])
  assert t.intervals == [Timescale.Interval(0, 1)]
  assert t.scattered_points == []

def test_overlapping_intervals():
  from timescalelib.core import Timescale

  intervals = [Timescale.Interval(0, 1), Timescale.Interval(0.5, 1.5)]
  scattered_points = []
  t = Timescale(intervals, scattered_points)

  assert t.intervals == [Timescale.Interval(0, 1.5)]
  assert t.scattered_points == []

def test_scattered_points_in_intervals():
  from timescalelib.core import Timescale

  intervals = [Timescale.Interval(0, 1)]
  scattered_points = [0.5, 1.5]
  t = Timescale(intervals, scattered_points)

  assert t.intervals == [Timescale.Interval(0, 1)]
  assert t.scattered_points == [1.5]

def test_duplicate_points():
  from timescalelib.core import Timescale

  scattered_points = [0.5, 0.5, 1.5]
  t = Timescale([], scattered_points)

  assert t.scattered_points == [1.5]

def test_forward_jump():
  from timescalelib.core import Timescale
  intervals = [Timescale.Interval(0, 1), Timescale.Interval(2, 3)]
  scattered_points = [1.5, 2.5]
  t = Timescale(intervals, scattered_points)

  assert t.forward_jump(0) == 0
  assert t.forward_jump(0.5) == 0.5
  assert t.forward_jump(1) == 1.5
  assert t.forward_jump(1.5) == 2
  assert t.forward_jump(2) == 2
  assert t.forward_jump(2.5) == 2.5
  assert t.forward_jump(3) == 3

def test_backward_jump():
  from timescalelib.core import Timescale
  intervals = [Timescale.Interval(0, 1), Timescale.Interval(2, 3)]
  scattered_points = [1.5, 2.5]
  t = Timescale(intervals, scattered_points)

  assert t.backward_jump(0) == 0
  assert t.backward_jump(0.5) == 0.5
  assert t.backward_jump(1) == 1
  assert t.backward_jump(1.5) == 1
  assert t.backward_jump(2) == 1.5
  assert t.backward_jump(2.5) == 2.5
  assert t.backward_jump(3) == 3

def test_graininess():
  from timescalelib.core import Timescale
  intervals = [Timescale.Interval(0, 1), Timescale.Interval(2, 3)]
  scattered_points = [1.5, 2.5]
  t = Timescale(intervals, scattered_points)

  assert t.graininess(0) == 0
  assert t.graininess(0.5) == 0
  assert t.graininess(1) == 0
  assert t.graininess(1.5) == 0.5
  assert t.graininess(2) == 0
  assert t.graininess(2.5) == 0.5
  assert t.graininess(3) == 0
