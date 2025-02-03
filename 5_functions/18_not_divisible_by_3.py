def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []
for numbers in [numbers_1, numbers_2, numbers_3, numbers_4]:
    if any(remainders_3(numbers)):
        print(f"{numbers} contains numbers not divisible by 3.")