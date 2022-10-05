from itertools import product

print("w x y z")

for w, x, y, z in product([0, 1], repeat=4):
    if not( (x and z) or ((not w or x) == (not z or y)) ):
        print(f"{w} {x} {y} {z}")        
