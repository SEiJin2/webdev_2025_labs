# function to calculate the sum of the 100 numbers from the input

# function to generate 100 random numbers in range of [1, 100]
import random
random_numbers = lambda: [random.randint(1, 100) for _ in range(100)]

def sum_of_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

# Example usage
if __name__ == "__main__":
    print("Sum of 100 random numbers")
    numbers = random_numbers()
    print("Generated numbers:", numbers)
    result = sum_of_numbers(numbers)
    print("Sum of numbers:", result)