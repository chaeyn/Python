n = int(input())
s = int(0)
for i in range(n-1):
    s = s+i
    if n<=s:
        print(i)
        break