V = []

def f(c, n, s):
    # 목표 상태
    if c == n:
        V.append(s)
        return

    # 탐색 종료
    if c > n:
        return

    # 다음 상태
    f(c + 1, n, s * 10 + 1)
    f(c + 2, n, s * 10 + 2)

    return

# 계단의 수 입력
n = int(input())

# 초기 상태
f(0, n, 0)

# 점프 방법 오름차순 정렬
V.sort()

# 점프 방법 출력
for num in V:
    print(num)
