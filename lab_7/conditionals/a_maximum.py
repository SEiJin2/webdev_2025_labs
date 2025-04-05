# lambda function to return the maximum of two input numbers

largest = lambda a, b: a if a > b else b

# Example usage
if __name__ == "__main__":
    print("Find the maximum of two numbers")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The maximum of {a} and {b} is {largest(a, b)}")