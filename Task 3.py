Numbers = [1, 4, 5, 10, 6, 9, 18]
print("The numbers in ", Numbers, "that are division by 2 are: ")
def count():
    for n in Numbers:
        if n % 2 == 0:
            print(n)
number = count()
