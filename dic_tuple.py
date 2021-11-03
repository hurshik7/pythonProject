board = {(0, 0): "nothing", (0, 1): "nothing", (1, 0): "nothing", (1, 1): "nothing"}
x_destination = 0
y_destination = 0
destination = (0, 0)

for coordinate in board.keys():
    if coordinate > destination:
        destination = coordinate


print(destination)
