n = int(input())
k = list(map(int, input().split()))
even = 0
odd = 0

for i in range(n):
    if k[i] % 2 == 0:
        even += k[i]
    else:
        odd += k[i]
print(even, odd)