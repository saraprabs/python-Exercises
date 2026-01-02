#Program to perform Arithmetic operations

num_1 = int(input("Emter First Number:"))

num_2 = int(input("Emter Second Number:"))

sum = num_1 + num_2

print(f"Sum of two numbers = {sum}")

diff = num_1 - num_2

print(f"Difference of two numbers = {diff}")

product = num_1 * num_2

print(f"Product of two numbers = {product}")

try:
    division = num_1 / num_2
    print(f"Division of two numbers = {division:.2f}")
except  ZeroDivisionError:
    print("Division by Zero")

power = num_1 ** num_2

print(f"{num_1} Power of {num_2} = {power}")

