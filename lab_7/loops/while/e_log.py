# lambda function to return a power of 2 so that it is more than or equal to n (e.g. 2^k >= n)
k = lambda n: (n - 1).bit_length() # using bitwise operation

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The smallest power of 2 greater than or equal to {n} is: {k(n)}")