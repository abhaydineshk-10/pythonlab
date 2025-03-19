print("=====Swap two variables=====")

x = input("Enter value of x: ")
y = input("Enter value of y: ")

temp = x
x = y
y = temp

print(f"Value of x after swapping: {x}")
print(f"Value of y after swapping: {y}")

print("=====Swap two variables using tuple unpacking=====")

x = input("Enter value of x: ")
y = input("Enter value of y: ")

y = y + x 
x = x - y
x = x - y

print(f"Value of x after swapping: {x}")
print(f"Value of y after swapping: {y}")