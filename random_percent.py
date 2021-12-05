import random

num_list = [1, 2, 3, 4]
random_number = random.sample(num_list, 1)
if random_number[0] == 4:
    print("25%")
else:
    print("75%")


