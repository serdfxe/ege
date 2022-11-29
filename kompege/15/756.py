a = 0

f = lambda x: x % a or (x % 28 or x % 42 == 0) 

while True:
    a += 1
    if all(f(i) for i in range(100000)):
        break

print(a)