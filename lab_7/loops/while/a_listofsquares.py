# function to find all valid squares from 1 to n using while loop
def squares(n):
    """Return a list of squares from 1 to n."""
    result = []
    i = 1
    while i <= n:
        if (i ** 0.5).is_integer():
            result.append(i)
        i+= 1
    return result

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The squares from 1 to {n} are: {squares(n)}")