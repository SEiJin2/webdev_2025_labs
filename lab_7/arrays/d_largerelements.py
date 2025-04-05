# lambda function to find a number of elements greater than the previous one in a list
greater_elements = lambda lst: len([lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]])

# Example usage
if __name__ == "__main__":
    lst = [int(i) for i in input("Enter numbers separated by space: ").split()]
    print(f"The elements greater than the previous one are: {greater_elements(lst)}")