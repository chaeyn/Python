n = int(input())
result, start = int(0), int(0)
while True:
    result += start
    start += 1
    if result>=n:
        break
print(result)