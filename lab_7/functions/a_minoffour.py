# function to find smallest element in a list without using built-in functions
def smallest(lst):
    if not lst:
        return None  # Return None if the list is empty
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

# Example usage
if __name__ == "__main__":
    lst = [int(i) for i in input("Enter numbers separated by space: ").split()]
    print(f"The smallest element in the list is: {smallest(lst)}")