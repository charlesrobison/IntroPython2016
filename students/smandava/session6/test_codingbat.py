"""Nov 26, 2016 Test cases for Coding bat exercises."""

from sm_codingbat import sum_double, parrot_trouble, string_times

# Test cases for sum_double.


def test_sum_double_same():
    assert sum_double(5, 5) == 20

def test_sum_double_diff():
    assert sum_double(5, 6) == 11

def test_sum_double_same_false():
    assert sum_double(6, 6) != 12

def test_sum_double_diff_false():
    assert sum_double(2, 3) != 10

# Test cases for parrot_trouble.


def test_parrot_trouble_true_6():
    assert parrot_trouble(True, 6) is True

def test_parrot_trouble_true_7():
    assert parrot_trouble(True, 7) is False

def test_parrot_trouble_true_20():
    assert parrot_trouble(True, 20) is False

def test_parrot_trouble_true_21():
    assert parrot_trouble(True, 21) is True

def test_parrot_trouble_false_20():
    assert parrot_trouble(False, 20) is False

def test_parrot_trouble_false_21():
    assert parrot_trouble(False, 21) is False


# Test cases for string_times.

def test_string_times_2():
    assert string_times('python', 2) == 'pythonpython'


def test_string_times_3():
    assert string_times('python', 3) != 'pythonpython'
