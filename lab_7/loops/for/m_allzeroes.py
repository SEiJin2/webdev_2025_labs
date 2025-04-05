# function to count the number of zeroes in a list
 
def zeroes_count(lst):
    result = 0
    for i in lst:
        if i == 0:
            result += 1
    return result

# Example usage
if __name__ == "__main__":
    print("Count the number of zeroes in a list")
    amount = int(input("Enter the amount of numbers: "))
    lst = [int(i) for i in input("Enter numbers separated by space: ").split()]
    result = zeroes_count(lst)
    print(result)

