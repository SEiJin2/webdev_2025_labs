# lambda function returning the reverse of a list
reverse_list = lambda lst: lst[::-1]

# Example usage
if __name__ == "__main__":
    lst = [int(i) for i in input("Enter numbers separated by space: ").split()]
    print(f"The reverse of the list is: {reverse_list(lst)}")