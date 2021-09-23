number = [13, 4, 12, 3, 5, 8, 7, 11, 6, 1]
print(number)

end_point = 9
current_point = 0
while end_point > 0:
    while current_point < end_point:
        if number[current_point] > number[current_point + 1]:
            temp = number[current_point]
            number[current_point] = number[current_point + 1]
            number[current_point + 1] = temp
        current_point += 1
    current_point = 0
    end_point -= 1

print(number)
