A = [[0] * 15 for _ in range(15)]
ans = 0

# 위
def f1(x, y, k):
    global ans
    if x == 0:
        return
    if A[x][y] <= k and A[x][y] >0:
        ans += 1
    f1(x-1, y, k)

# 아래
def f2(x, y, k):
    global ans
    if x == 11:
        return
    if A[x][y] <= k and A[x][y] >0:
        ans += 1
    f2(x+1, y, k)

# 왼
def f3(x, y, k):
    global ans
    if y == 0:
        return
    if A[x][y] <= k and A[x][y] >0:
        ans += 1
    f3(x, y-1, k)

# 오
def f4(x, y, k):
    global ans
    if y == 11:
        return
    if A[x][y] <= k and A[x][y] >0:
        ans += 1
    f4(x, y+1, k)

# 공격력 입력
k = int(input())
x, y = 0, 0

# 맵 정보 입력
for i in range(1, 11):
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        A[i][j + 1] = value
        if value == -1:
            x = i
            y = j + 1

f1(x - 1, y, k) # 위로 탐색
f2(x + 1, y, k) # 아래로 탐색
f3(x, y - 1, k) # 왼쪽 탐색
f4(x, y + 1, k) #오른쪽 탐색
print(ans) # 쓰러지는 몬스터의 수를 출력