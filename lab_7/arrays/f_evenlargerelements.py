# lambda function to count array elements that are larger than their neighbors
larger_neighbors = lambda arr: len([arr[i] for i in range(1, len(arr) - 1) if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]])

# Example usage
if __name__ == "__main__":
    arr = [int(i) for i in input("Enter numbers separated by space: ").split()]
    print(f"The number of elements larger than their neighbors is: {larger_neighbors(arr)}")