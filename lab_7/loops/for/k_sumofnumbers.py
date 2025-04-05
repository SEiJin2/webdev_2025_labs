# function to calculate all input numbers based on the first number

def sum_of_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def input_numbers(n):
    numbers = []
    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)
    return numbers

# Example usage
if __name__ == "__main__":
    print("Find the sum of n numbers")
    n = int(input("Enter the number of elements: "))
    numbers = input_numbers(n)
    result = sum_of_numbers(numbers)
    print(f"The sum of the numbers is: {result}")