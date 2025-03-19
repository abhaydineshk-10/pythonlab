import math

number = int(input("Enter a number: "))

if number <= 1:
    print("The number is not prime.")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
