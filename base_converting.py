number_in_base10 = int(input("input your number in base 10 : "))
if number_in_base10 < 0:
    number_in_base10 = int(input("input a positive number : "))

destination_base = int(input("input destination base : "))
if destination_base < 2 or destination_base > 9:
    destination_base = int(input("input a number between 2 and 9"))

number_in_base_b = ""
while number_in_base10 != 0:
    dividend = number_in_base10 % destination_base
    number_in_base10 = number_in_base10 // destination_base
    number_in_base_b += str(dividend)

print(number_in_base_b)
