# lambda function to calculate lowered down number - result of division

down = lambda x, y: x // y

# example usage
if __name__ == "__main__":
    print("Calculate the lowered down number")
    x = int(input("Enter the dividend: "))
    y = int(input("Enter the divisor: "))
    print(f"The lowered down number of {x} divided by {y} is {down(x, y)}")

