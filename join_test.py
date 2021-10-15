import random
import string


def name(length):
    first_letter = "".join(random.sample(string.ascii_uppercase, 1))
    random_name_without_first_letter = "".join(random.sample(string.ascii_lowercase, length -1))
    random_name = first_letter + random_name_without_first_letter
    return random_name

random_str = name(2)
print(random_str)

