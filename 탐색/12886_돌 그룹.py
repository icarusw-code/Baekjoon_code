from collections import deque

stone_a, stone_b, stone_c = map(int, input().split())
total = stone_a + stone_b + stone_c
check = [[False] * total for _ in range(total)]

def bfs():
    queue = deque()
    queue.append((stone_a, stone_b))
    check[stone_a][stone_b] = True

    while queue:
        x, y = queue.popleft()
        z = total - x - y
        if x == y == z:
            print(1)
            return
        for a, b in (x, y), (y, z), (x, z):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else:
                continue
            c = total - a - b
            case_min = min(a, b, c)
            case_max = max(a, b, c)
            if not check[case_min][case_max]:
                queue.append((case_min, case_max))
                check[case_min][case_max] = True
    print(0)

def game():
    if total % 3 != 0 :
        print(0)
        return
    else:
        bfs()

game()