# lambda function to calculate remainder of division

remainder = lambda x, y: x % y

# example usage
if __name__ == "__main__":
    print("Calculate the remainder of division")
    x = int(input("Enter the dividend: "))
    y = int(input("Enter the divisor: "))
    print(f"The remainder of {x} divided by {y} is {remainder(x, y)}")