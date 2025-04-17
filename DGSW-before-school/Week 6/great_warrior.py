ans = 0

def f(c):
    global ans
    if c <= 0:
        ans += 1
    f(c - 1)
    f(c - 3)

n = int(input())
f(n)
print(ans)
