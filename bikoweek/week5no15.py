a = [list(map(int, input().split())) for _ in range(2)]
b = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    for j in range(2):
        if i == j == 0:
            print((a[0][0] * b[0][0]) + (a[0][1] * b[1][0]) , end=' ')
        elif i == 0 and j == 1:
            print((a[0][0] * b[0][1]) + (a[0][1] * b[1][1]) , end=' ')
        elif i == 1 and j == 0:
            print((a[1][0] * b[0][0]) + (a[1][1] * b[1][0]) , end=' ')
        elif i == 1 and j == 1:
            print((a[1][0] * b[0][1]) + (a[1][1] * b[1][1]) , end=' ')
    print()