# function to find all powers of two from 1 to n using while loop
def powers_of_two(n):
    """Return a list of powers of two from 1 to n."""
    result = []
    i = 1
    while i <= n:
        result.append(i)
        i *= 2
    return result

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The powers of two from 1 to {n} are: {powers_of_two(n)}")