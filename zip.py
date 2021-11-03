import itertools

pairs = []
names = ("Victoria", "Edmonton", "Regina", "The Peg")
for pair in zip(itertools.count(1), names):
    pairs.append(pair)

print(pairs)

#1 Victoria

