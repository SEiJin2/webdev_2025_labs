# lambda function that checks of a number is a power of two
is_power_of_two = lambda n: n > 0 and (n & (n - 1)) == 0 # using bitwise operation

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_power_of_two(n):
        print(f"{n} is a power of two.")
    else:
        print(f"{n} is not a power of two.")