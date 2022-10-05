from itertools import product

print("w x y z")

for w, x, y, z in product((0, 1), repeat=4):
    if (x or not y) and not (y == z) and w:
        print(w, x, y, z)