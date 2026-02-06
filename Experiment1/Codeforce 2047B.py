import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
 
    if n == 1:
        print(s)
        continue
 
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
 
    maxFreq = -1
    minFreq = 11  
    maxChar = ' '
    minChar = ' '
 
    for i in range(26):
        if freq[i] > 0:
            if freq[i] >= maxFreq:
                maxFreq = freq[i]
                maxChar = chr(i + ord('a'))
            if freq[i] <= minFreq:
                minFreq = freq[i]
                minChar = chr(i + ord('a'))
 
    if minChar == maxChar:
        for i in range(26):
            if freq[i] > 0 and chr(i + ord('a')) != maxChar:
                minChar = chr(i + ord('a'))
                break
 
    res = list(s)
    for i in range(n):
        if res[i] == minChar:
            res[i] = maxChar
            break
 
    print("".join(res))
