# lambda function to find all even elements in a list
even_elements = lambda lst: [x for x in lst if x % 2 == 0]

# Example usage
if __name__ == "__main__":
    lst = [int(i) for i in input("Enter numbers separated by space: ").split()]
    print(f"The even elements of the list are: {even_elements(lst)}")