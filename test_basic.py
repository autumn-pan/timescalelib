from timescalelib import TimeScale, Interval

def test_construction():
    ts = TimeScale([Interval(1, 4), Interval (2, 3), Interval (8,9), Interval(3, 6), Interval(-1, 2)], [2,5,5])
    print(ts.__repr__())


test_construction()
