# hackerrank list comprehension problem

def main():

    x, y, z = map(int, input().split())
    p = map(int, input())

    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != p]

    # Print the result
    print(coordinates)

if __name__ == "__main__":
    main()