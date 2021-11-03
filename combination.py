import itertools

size = 2
combos = list(itertools.combinations(["ginger", "appspice", "cumin", "mint"], 2))
print(combos)

for seq, combo in enumerate(combos, 1):
    print("%d:\t%s" % (seq, combo))
