def swap(a, b):
    temp = a
    a = b
    b = a
    a[0] = 999



test_list = ['a', 'b', 'c']
test_list_2 = [1, 2, 3]
swap(test_list, test_list_2)

print("test_list : %s" % test_list)
print("test tuple : %s" % test_list_2)

