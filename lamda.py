def square(x):
    return x ** 2

print(square(5))

def add(a, b):
    return a + b

print(add(3, 4))

numbers = [5, 3, 8, 6, 7, 2]
square_numbers =[x ** 2 for x in numbers]
print(square_numbers)