# lambda function representing the XOR operation (avoided using ^ operator)
def xor(a, b):
    return bool((a and not b) or (not a and b))

# Example usage
if __name__ == "__main__":
    a = int(input("Enter first number (0 or 1): "))
    b = int(input("Enter second number (0 or 1): "))
    print(f"The result of XOR operation between {a} and {b} is: {xor(a, b)}")