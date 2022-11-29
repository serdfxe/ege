from itertools import product

print("x y z w F")

for x, y, z, w in product((0, 1), repeat=4):
    if ((x or (y and not z)) and not w):
        print(x, y, z, w)