# lambda function to find total numbers of divisors of a number n

amount_of_divisors = lambda n: len([i for i in range(1, n + 1) if n % i == 0])

# Example usage
if __name__ == "__main__":
    print("Find total numbers of divisors of a number")
    n = int(input("Enter a number: "))
    result = amount_of_divisors(n)
    print(result)