import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 4:
        print(-1)
        continue
    evens = []
    odds = []
    for i in range(1, n + 1):
        if i % 2 == 0 and i != 4:
            evens.append(i)
        elif i % 2 == 1 and i != 5:
            odds.append(i)
    result = evens + [4, 5] + odds
    print(*result)
