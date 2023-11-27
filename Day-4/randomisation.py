# Randomisation

import random

random_integer = random.randint(1, 10) # random integer between 1 and 10
random_float = random.random() # random float between 0 and 1 
random_float_2 = random.random() * 5 # random float between 0 and 5
love_score = random.randint(1, 100)

print(f"Your love score is {love_score}%")