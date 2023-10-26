score = int(input("Enter the quiz score: "))

grade = 'Undefined'

grades = {
    5: 'A',
    4: 'B',
    3: 'C',
    2: 'D',
    1: 'F',
    0: 'F'
}

for key, value in grades.items():
    if score == key:
        grade = value
        break

print("The letter grade is:", grade)