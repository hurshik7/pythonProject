import itertools

primary_colours = ['cyan', 'magenta', 'yellow']
permutations = itertools.permutations(primary_colours)
permutations_list = list(permutations)

print(type(permutations))
print()
print(permutations_list)
print()

print(len(permutations_list))

print("permutations_list[0] : ", permutations_list[0])
print("type(permutations_list[0]) : ", type(permutations_list[0]))

for sequence_number, permutation in enumerate(permutations_list, 1):
    print("%d:\t%s" % (sequence_number, permutation))
    print(type(permutation))

