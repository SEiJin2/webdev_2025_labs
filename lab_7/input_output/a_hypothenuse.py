# lambda function to calculate the hypotenuse of a right triangle

import math
hypotenuse = lambda a, b: math.sqrt(a**2 + b**2)

# Example usage
if __name__ == "__main__":
    print("Calculate the hypotenuse of a right triangle")
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    print(f"The hypotenuse of a right triangle with sides {a} and {b} is {hypotenuse(a, b)}")