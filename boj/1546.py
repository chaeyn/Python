n = int(input())

maximum = 0
res = 0

for i in range(n):
    m = int(input())
    if m >= maximum:
        maximum = m
for i in range(n):
    if m[i] < maximum:
        m[i] = m[i]/maximum*100
    res += m[i]
print(res)