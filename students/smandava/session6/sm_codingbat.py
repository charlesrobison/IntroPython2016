# Nov 6, 2016 Test Driven Development.

# sum_double from warmup-1 in codingbat.
def sum_double(a, b):
    """Unless the two values are the same, then return double their sum."""
    if (a == b):
        return (2 * (a + b))
    else:
        return(a + b)


# parrot_trouble from warmup-1 in codingbat
def parrot_trouble(talking, hour):
    """ Return true if the parrot is talking and the hour is before 7 or after 20."""
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


# String_time from warmup-2 in codingbat
def string_times(str, n):
    """ Return string that is n copies of the original string."""
    if (n >= 0):
        return (str * n)

# TODO:Sum 67 from list-2 in codingbat
def sum67(nums):
    sum = 0
    for num in nums:
        if (num == 6):
            continue
        elif (num == 7):
            continue
    sum =+ num

