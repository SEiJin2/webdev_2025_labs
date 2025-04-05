# lambda function to check if there are two neighboring elements in a list that have the same sign
same_sign_neighbors = lambda lst: any((lst[i] > 0 and lst[i + 1] > 0) or (lst[i] < 0 and lst[i + 1] < 0) for i in range(len(lst) - 1))

# Example usage
if __name__ == "__main__":
    lst = [int(i) for i in input("Enter numbers separated by space: ").split()]
    print(f"Are there two neighboring elements with the same sign? {same_sign_neighbors(lst)}")