# function to check if the solution is correct

def test_system(a: int, b: int) -> str:
    if a != 1 and b != 1:
        return "YES"
    elif a == 1 and b == 1:
        return "YES"
    else:
        return "NO"
    
# example usage
if __name__ == "__main__":
    print("Test system")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The test system is {test_system(a, b)}")