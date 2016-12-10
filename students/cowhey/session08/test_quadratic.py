from quadratic import Quadratic

def test_quad():
    q = Quadratic(1, 2, 3)
    assert q(3) == 18
    q2 = Quadratic(1, 1, 1)
    assert q2(1) == 3


def test_neg_quad():
    q = Quadratic(-1, 1, 4)
    assert q(3) == -2
    assert q(-2) == -2
