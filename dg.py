import random
import os


def generate():

    # Input the number of random numbers to generate
    n = int(input("Enter the value of n: "))

    x = input("Enter filename:\t")
    x = x+".txt"

    # Output file name
    filename = os.path.join("datasets", x)

    # Generate and write random numbers
    with open(filename, "w") as file:
        for _ in range(n):
            # Random integer between 1 and n
            number = random.randint(-10000, 10000)
            file.write(f"{number}\n")

    print(f"{n} random numbers have been written to '{filename}'.")
    return x
