first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))

def multiply(first_num: float, second_num: float) -> float:
    return first_num * second_num

product = multiply(first_num, second_num)
print(f"{first_num} * {second_num} = {product}")