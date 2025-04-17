ans = 0

def f(c, n):
    global ans

    # 목표 상태
    if c == n:
        ans += 1
        return

    # 탐색 종료
    if c >= n:
        return

    # 다음 상태
    f(c + 1, n)
    f(c + 2, n)

    return

# 계단의 수 입력
n = int(input())

# 초기 상태
f(0, n)

# 경우의 수 출력
print(ans)
