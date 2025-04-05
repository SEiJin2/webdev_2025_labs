# lambda function to check if the first or second number is the largest
largest = lambda a, b: 1 if a > b else 2

# Example usage
if __name__ == "__main__":
    print("Find the largest number")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = largest(a, b)
    print(result)