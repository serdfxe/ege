from functools import lru_cache

@lru_cache(None)
def f(s, e, i=None):
    if s == e: return 1
    if s > e or s == i: return 0
    return f(s + 1, e, i) + f(s + 2, e, i)

# print(f(11, 29))

print(f(11, 17) * f(17, 29, 23) + f(11, 23, 17) * f(23, 29) + f(11, 17) * f(17, 23) * f(23, 29))
