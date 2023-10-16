"""
Define a function called count_evens.

The count_evens function accepts a non-empty list of integers called readings.

The count_evens function must return a tuple that contains two integers.
The first value in the tuple must be the number of even integers in the list called readings.
The second value must be the sum of the even integers in the list called readings.

You may not modify the list passed as an argument in any way, even temporarily, if you do you
will earn zero marks for this question.

You must provide a full docstring for this function including all pre- and post-conditions.
You must create two useful and different doctests for this function.
No main function is required.
"""


def count_evens(readings):
    """
    Count even integers in the list.

    This function counts the number of even integers and calculates the sum of the even integers in the list called
    readings.

    :param readings: a non-empty list of integers
    :precondition: readings must be a non-empty list of integers
    :postcondition: count the number of even integers and calculate the sum of the even integers in the list
    :return: a tuple, with 2 values.
    >>> count_evens([-12, -333, 0, 2, 6, 7, 323, 999])
    (4, -4)
    >>> count_evens([-99, -2, 0, 444, 9, 13])
    (3, 442)
    """
    even_integer_count = 0
    even_integer_sum = 0
    for integer in readings:
        if integer % 2 == 0:
            even_integer_count += 1
            even_integer_sum += integer

    even_integer = (even_integer_count, even_integer_sum)
    return even_integer
