
dict1 = { 'length':2, 0:-1, 1:1, 2:1 }
dict2 = { 'length':2, 0:1, 1:1 }


if (dict1['length'] != dict2['length']):
    print("Invalid")


new_dict = {}
for key, value in dict1.items():
    new_dict[key] = value


for key in dict2:
    if key != 'length':
        if key not in new_dict:
            new_dict[key] = 0
        new_dict[key] += dict2[key]
        if new_dict[key] == 0:
            del(new_dict[key])


print(dict1)
print(dict2)
print("new_dict : ", new_dict)
sorted(new_dict)
