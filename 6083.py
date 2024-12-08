r, g, b = map(int, input().split())
count = int(0)
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print('%d %d %d' %(i, j, k))
            count = count+1
print(count)