n, a = map(int, input().split())
for i in range (n):
    if (i+1)%a == 0 :
        print(i+1, end=' ')