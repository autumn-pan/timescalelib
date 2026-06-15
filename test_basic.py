from timescalelib import TimeScale, Interval, integrals, derivatives, generators

import math

def is_close(a, b, tol=1e-3):
    return abs(a - b) < tol

def test_construction():
    ts = TimeScale([Interval(1, 4), Interval (2, 3), Interval (8,9), Interval(3, 6), Interval(-1, 2)], [2,5,5])
    print(ts.__repr__())

def test_forward_jump():
    ts = TimeScale([], [1, 2, 3])
    assert ts.forward_jump(0) == 1
    assert ts.forward_jump(1) == 2
    assert ts.forward_jump(2) == 3
    assert ts.forward_jump(3) == 3

def test_backward_jump():
    ts = TimeScale([], [1, 2, 3])
    assert ts.backward_jump(0) == 0
    assert ts.backward_jump(1) == 1
    assert ts.backward_jump(2) == 1
    assert ts.backward_jump(3) == 2

def test_interval_jump():
    ts = TimeScale([Interval(1, 4)], [])
    assert ts.forward_jump(0) == 1
    assert ts.forward_jump(1) == 1
    assert ts.forward_jump(2) == 2
    assert ts.forward_jump(3) == 3
    assert ts.forward_jump(4) == 4
    assert ts.forward_jump(5) == 5

    assert ts.backward_jump(0) == 0
    assert ts.backward_jump(1) == 1
    assert ts.backward_jump(2) == 2
    assert ts.backward_jump(3) == 3
    assert ts.backward_jump(4) == 4
    assert ts.backward_jump(5) == 4

def test_graininess():
    ts = TimeScale([Interval(1, 4)], [5])
    assert ts.grain(1) == 0
    assert ts.grain(2) == 0
    assert ts.grain(3) == 0
    assert ts.grain(4) == 1
    assert ts.grain(5) == 0

    assert ts.backwards_grain(1) == 0
    assert ts.backwards_grain(2) == 0
    assert ts.backwards_grain(3) == 0
    assert ts.backwards_grain(4) == 0
    assert ts.backwards_grain(5) == 1

def test_integrals():
    ts = TimeScale([Interval(0, 1)], [2, 3])
    f = lambda x: x**2
    assert is_close(integrals.delta_integral(ts, f, 0, 1), 1/3)
    assert is_close(integrals.nabla_integral(ts, f, 0, 1), 1/3)

test_integrals()

print("All tests passed!")