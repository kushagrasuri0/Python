print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
rows = 5
for i in range(rows):
    for j in range(rows):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
