"""

"""


def cleaner(measurements, maximum):
    """
    Create a new list with numbers in the old list less than maximum.

    :param measurements: a non-empty list with floats
    :param maximum: a float
    :precondition: measurements must be a non-empty list with floats
    :precondition: maximum must be a float
    :postcondition: new list contains numbers in the old list less than maximum
    :return: a list, with numbers in the old list less than maximum
    >>> cleaner([-8.8, -3.4, 1.01, 5.4], 1.1)
    [-8.8, -3.4, 1.01]
    >>> cleaner([-93.82, -9.4, -1.33, 435.4], -9.777)
    [-93.82]
    """
    less_than_maximum = []
    for number in measurements:
        if number < maximum:
            less_than_maximum.append(number)

    return less_than_maximum


def main():
    print('For list [0.0, 1.2, 2.3, 8.8, 10.1], when maximum is 9.1, '
          'the new list will be', cleaner([0.0, 1.2, 2.3, 8.8, 10.1], 9.1))
    print('For list [-0.9, -33, 0.11, 2.43, 9.55], when maximum is 0.1,'
          'the new list will be', cleaner([-0.9, -33, 0.11, 2.34, 9.55], 0.1))


if __name__ == "__main__":
    main()
