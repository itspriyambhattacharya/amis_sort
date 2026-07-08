from sort import bubbleSort
from dg import generate
import os


def main():
    x = generate()
    filename = os.path.join("datasets", x)
    with open(filename, "r") as f:
        lst = [int(x) for x in f.read().split()]

    n = len(lst)
    print("\nThe Array is:")
    print(lst)
    print("\nThe sorted list is:")
    bubbleSort(lst, 0, n-1)
    print(lst)

    with open("output.txt", "w") as f:
        f.write(" ".join(str(x) for x in lst))

    print("\nSorted array written to output.txt")


if __name__ == '__main__':
    main()
