# division on hackerrank

def main():
    # Read two integers from input
    a, b = map(int, input("Enter two integers: ").split())
    
    # Perform division and print results
    print(a // b)  # Floor division
    print(a / b)   # True division

# Example usage
if __name__ == "__main__":
    main()