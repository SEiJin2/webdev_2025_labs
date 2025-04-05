# lambda function to determine if a number is weird or not
is_weird = lambda n: (n % 2 == 1) or (n % 2 == 0 and 6 <= n <= 20)

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_weird(n):
        print("Weird")
    else:
        print("Not Weird")