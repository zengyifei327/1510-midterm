"""

"""


def prime(number):
    if number == 1:
        return False

    else:
        divisor = number - 1
        while divisor > 1:
            # check if the number can be divided by numbers other than itself and 1 without remainders
            if number % divisor == 0:
                return False
            divisor -= 1
        return True


def sum_of_primes(lower_bound, upper_bound):
    sum_result = 0
    for number in range(lower_bound, upper_bound + 1):
        if prime(number):
            sum_result += number
    return sum_result


def main():
    print(sum_of_primes(10, 20))


if __name__ == "__main__":
    main()
