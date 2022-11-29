with open("kompege/24/3743.txt") as f: s = f.read().strip()

# print(s[:10])

s = s.replace("A", "aa").replace("B", "bb").replace("C", "cc")

l = ["ab", "cb", "bc", "ba"]

for i in range(4):
    s = s.replace(l[i], "1")

ans = 0

for i in range(1, len(s)):
    if "1" * i in s:
        ans = i
        print(i)

print(ans)
