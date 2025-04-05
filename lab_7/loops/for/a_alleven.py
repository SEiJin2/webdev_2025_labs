# lambda function to return all even numbers between input a and b
numbers = lambda a, b: [i for i in range(a, b + 1) if i % 2 == 0]

# Example usage
if __name__ == "__main__":
    print("Find all even numbers between a and b")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = numbers(a, b)
    print(result)