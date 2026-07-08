from sort import mergeSort
import os
from dg import generate


def main():
    x = generate()
    filename = os.path.join("datasets", x)
    with open(filename, "r") as f:
        lst = [int(x) for x in f.read().split()]

    n = len(lst)

    print("\nThe Array is:")
    print(lst)

    mergeSort(lst, 0, n - 1)

    print("\nThe sorted list is:")
    print(lst)

    with open("output.txt", "w") as f:
        f.write(" ".join(str(x) for x in lst))

    print("\nSorted array written to output.txt")


if __name__ == "__main__":
    main()
