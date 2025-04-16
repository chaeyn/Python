import sys
input = sys.stdin.readline

n,m = map(int,input().split())
li = {}
for i in range(n):
    s,s1 = input().split()
    li[s]=s1
result = []
for i in range(m):
    q = input().strip()
    result.append(li[q])
print("\n".join(result))
