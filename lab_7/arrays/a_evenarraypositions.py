# function to return the even indexed elements of an array
def even_array_positions(arr):
    return [arr[i] for i in range(len(arr)) if i % 2 == 0]

# Example usage
if __name__ == "__main__":
    arr = [int(i) for i in input("Enter numbers separated by space: ").split()]
    print(f"The even indexed elements of the array are: {even_array_positions(arr)}")