n1 = 1
n2 = 1
n_current = 2
nth_number = 0
n_input_by_user = -1
n_input_by_user = int(input("input n : "))

while n_input_by_user <= 0:
    print("please input positive number!")
    n_input_by_user = int(input("input n : "))

if n_input_by_user == 1:
    nth_number = n1
elif n_input_by_user == 2:
    nth_number = n2
else:
    while n_current != n_input_by_user:
        n_current += 1
        nth_number = n1 + n2
        n1 = n2
        n2 = nth_number

print("%dth number is : " % n_input_by_user, nth_number)

