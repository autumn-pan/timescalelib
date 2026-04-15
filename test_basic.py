from timescalelib import TimeScale, Interval

def test_construction():
    ts = TimeScale([Interval(1, 4)], [5])
    assert ts.intervals == [Interval(1, 4)]
    assert ts.scattered_points == [5]

test_construction()