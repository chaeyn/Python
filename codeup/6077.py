n = int(input())
s, r = int(0), int(0)
for i in range(n+1):
    if i%2==0:
        r = r + i
print(r)