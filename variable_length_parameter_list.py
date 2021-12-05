
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)
        print(type(topping))

    print(toppings)


make_pizza('green peppers')
make_pizza("ham", "pineapple", "garlic")

