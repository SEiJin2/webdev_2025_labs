# lambda function to receive numbers [a, b, c, d] and return all numbers that are divisible on the d in range of [a, b]
numbers = lambda a, b, c, d: [i for i in range(a, b + 1) if i % d == 0]

# Example usage
if __name__ == "__main__":
    print("Find all numbers between a and b that are divisible by d")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = int(input("Enter fourth number: "))
    result = numbers(a, b, c, d)
    print(result)