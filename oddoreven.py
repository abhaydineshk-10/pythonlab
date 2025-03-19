def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = check_odd_or_even(num)
    print(f"The number {num} is {result}.")