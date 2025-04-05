# lambda function to find the minimum divisor of a number in range of [2, 30000]

minimum_divisor = lambda n: next((i for i in range(2, 30001) if n % i == 0), None)

# Example usage
if __name__ == "__main__":
    print("Find the minimum divisor of a number")
    n = int(input("Enter a number: "))
    result = minimum_divisor(n)
    if result is not None:
        print(f"The minimum divisor of {n} is {result}")
    else:
        print(f"{n} has no divisors in the range [2, 30000]")