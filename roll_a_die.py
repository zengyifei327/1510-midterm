import random


def roll_dice():
    roll_time = 0
    roll_result = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    while roll_time < 1000000:
        roll_one_time_result = random.randint(1, 6)
        roll_result[roll_one_time_result] += 1
        roll_time += 1
    return roll_result


def main():
    print(roll_dice())


if __name__ == "__main__":
    main()
