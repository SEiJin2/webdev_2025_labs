# function to calculate the power of a number without using the ** operator
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage
if __name__ == "__main__":
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")