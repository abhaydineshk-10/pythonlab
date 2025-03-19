num = int(input("Enter a number: "))
n = num

factorial = 1

while n > 0:
    factorial *= n
    num -= 1
    
    print(f"Factorial of {num} is {factorial}")