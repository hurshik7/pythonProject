cm_per_inch = 2.54
inches_per_foot = 12

def height_US_to_cm(feet, inches):
    print(cm_per_inch)
    print(inches_per_foot)
    cm_per_inch = 1
    total_inches = (feet * inches_per_foot) + inches
    cm = total_inches * cm_per_inch
    return cm

feet = int(input("Enter feet: "))
inches = int(input("Enter inches : "))

height_US_to_cm(feet, inches)

print("It works!")

