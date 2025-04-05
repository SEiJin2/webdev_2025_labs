# boolean lambda function to check if a year is a leap year

is_leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
if __name__ == "__main__":
    year = int(input())
    print(is_leap_year(year))