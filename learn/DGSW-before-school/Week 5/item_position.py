n = int(input())
items = list(map(int, input().split()))
target = int(input())
result = -1
for i in range(n):
    if items[i] == target:
        result = i + 1
        break
print(result)