# function to find the smallest divisor of a number using while loop
def smallest_divisor(n):
    """Return the smallest divisor of n."""
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The smallest divisor of {n} is: {smallest_divisor(n)}")