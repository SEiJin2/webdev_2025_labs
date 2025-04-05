 # lambda function to return an array of valid squares in range of [a, b]

squares = lambda a, b: [i for i in range(a, b + 1) if (i ** 0.5).is_integer()]

# Example usage
if __name__ == "__main__":
    print("Find all squares between a and b")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = squares(a, b)
    print(result)