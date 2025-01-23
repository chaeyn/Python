n = int(input())
age = list(map(int, input().split()))
value = 0
for i in range(n):
    if age[i] > 8:
        value = value + 1000
print(value)
