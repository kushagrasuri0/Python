print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
import random
flips = int(input("Enter coin flips: "))
results = []
streak = 0
maximum = 0
for _ in range(flips):
    flip = random.choice(['H', 'T'])
    results.append(flip)
    if len(results) > 1 and results[-1] == results[-2]:
        streak += 1
    else:
        streak = 1
    if streak > maximum:
        maximum = streak
print("Results:", results)
print("Longest streak:", maximum)
