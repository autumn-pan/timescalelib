from timescalelib import TimeScale, Interval

def test_construction():
    ts = TimeScale([Interval(1, 4), Interval (2, 3), Interval (8,9), Interval(3, 6), Interval(-1, 2)], [2,5,5])
    print(ts.__repr__())

def test_forward_jump():
    ts = TimeScale([], [1, 2, 3])
    assert ts.forward_jump(0) == 1
    assert ts.forward_jump(1) == 2
    assert ts.forward_jump(2) == 3
    assert ts.forward_jump(3) == 3

test_construction()
test_forward_jump()