# lambda function to count all positive elements in a list
positive_elements = lambda lst: len([x for x in lst if x > 0])

# Example usage
if __name__ == "__main__":
    lst = [int(i) for i in input("Enter numbers separated by space: ").split()]
    print(f"The number of positive elements in the list is: {positive_elements(lst)}")