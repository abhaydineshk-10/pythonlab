# Global variable
counter = 0

def modify_counter():
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

# Example usage
print(f"Counter before function call: {counter}")
modify_counter()
print(f"Counter after function call: {counter}")