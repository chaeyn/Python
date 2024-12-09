h, w = input().split() #격자판 크기 입력
h = int(h)
w = int(w)

size = [] # 격자판 생성
for i in range(h+1):
    size.append([])
    for j in range(w+1):
        size[i].append(0)

n = input() # 막대의 개수, 길이, 크기 등 입력 
n = int(n)
for i in range(n):
    l, d, x, y = map(int, input().split())

    if d == 0:
        for j in range(l):
            size[x][y+j] = 1
    else:
        for j in range(l):
            size[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(size[i][j], end=' ')
    print()