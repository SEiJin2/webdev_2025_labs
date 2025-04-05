# lambda function to get the next and previous numbers 

def next_and_prev(n):
    return (n - 1, n + 1)

# Example usage
if __name__ == "__main__":
    print("Get the next and previous numbers")
    n = int(input("Enter a number: "))
    prev_num, next_num = next_and_prev(n)
    print(f"The previous number is {prev_num} and the next number is {next_num}")