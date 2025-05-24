print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
# Coin Flip Streaks

import random

# Variables
num_flips = 50
streak = 0
last_flip = None
streaks = []
for flip in range(num_flips):
    coin = random.choice(['H', 'T'])
    if coin == last_flip:
        streak += 1
    else:
        if streak > 0:
            streaks.append(streak)
        streak = 1  
    last_flip = coin
if streak > 0:
    streaks.append(streak)
print("Coin Flip Streaks:", streaks)
