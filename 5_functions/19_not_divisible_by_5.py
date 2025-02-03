def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []
for numbers in [numbers_1, numbers_2, numbers_3, numbers_4]:
    if any(remainders_5(numbers)):
        print(f"{numbers} contains numbers not divisible by 5.")