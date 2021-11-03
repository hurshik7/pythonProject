
dics = { 0: "hurshik", 1: "mina" }
for index, dic in enumerate(dics.items(), 50):
    print(index, dic)

print(type(dics.keys()))
print(type(dics.items()))
print(type(dics.values()))

keys = dics.keys()
values = dics.values()
entries = dics.items()

print(keys)
print(values)
print(entries)
