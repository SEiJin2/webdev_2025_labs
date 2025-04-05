# lambda function to pring a sequence of numbers less than n as a string

sequence = lambda n: ''.join(str(i) for i in range(1, n+1))

# Example usage
if __name__ == "__main__":
    n = int(input())
    print(sequence(n))