def get(n):
    b = bin(n)[2:]
    s = ("0"*(8 - len(b)) + b)[::-1]

    return n - int(s, 2)

l = [get(i) for i in range(0, int("11111111", 2)+1)]

print(max(l))