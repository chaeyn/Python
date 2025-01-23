n, a = map(int, input().split())
product = list(map(int, input().split()))
result = 0
result = int(result)
for i in range(n):
    if product[i] > a:
        result += 1
print(result)