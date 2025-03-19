def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == "__main__":
    numbers = [10, 24, 45, 99, 2, 78, 56]
    largest_number = find_largest_number(numbers)
    if largest_number is not None:
        print(f"The largest number in the list is: {largest_number}")
    else:
        print("The list is empty.")