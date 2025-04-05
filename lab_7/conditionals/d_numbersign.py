# lambda function to test if a sign of a number is positive, negative or zero
positive_or_negative = lambda x: 1 if x > 0 else -1 if x < 0 else 0

# Example usage
if __name__ == "__main__":
    print("Check if a sign of a number is positive, negative or zero")
    x = int(input("Enter a number: "))
    result = positive_or_negative(x)
    print(result)