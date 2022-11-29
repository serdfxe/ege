from functools import lru_cache

@lru_cache(None)
def moves(s):
    return (s - 1, s // 2) if s % 2 == 0 else (s - 1,)

@lru_cache(None)
def game(s):
    if s <= 12:
        return "w"

    if any(game(i) == "w" for i in moves(s)):
        return "p1"

    if all(game(i) == "p1" for i in moves(s)):
        return "v1"

    if any(game(i) == "v1" for i in moves(s)):
        return "p2"

    if all(game(i) in ("p2", "p1") for i in moves(s)):
        return "v2!!!!!!!!"

    return "#"

for i in range(12, 100):
    print(i, game(i))