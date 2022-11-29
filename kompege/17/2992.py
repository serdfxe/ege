from functools import lru_cache
with open("kompege/17/2992.txt") as f: s = f.readlines()

s = [int(i) for i in s]

# print(s[:10])

m = max(i for i in s if i % 107 == 0)

# print(m)

n = 0

ans = 0

@lru_cache(None)
def get(n):
    s = []

    while n:
        s.append(n % 7)
        n //= 7

    return "".join(map(str, s[::-1]))

for i in range(len(s) - 1):
    ii = i + 1
    if (s[i] > m or s[ii] > m) and ("36" in get(s[i]) or "36" in get(s[ii])):
        if ans == 0 or s[i] + s[ii] < ans:
            ans = s[i] + s[ii]
            
        n += 1

print(n, ans)
