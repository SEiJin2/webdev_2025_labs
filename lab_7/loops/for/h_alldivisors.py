# lambda function to return an array of all divisors of a number

divisors = lambda n: [i for i in range(1, n + 1) if n % i == 0]

# Example usage
if __name__ == "__main__":
    print("Find all divisors of a number")
    n = int(input("Enter a number: "))
    result = divisors(n)
    print(result)