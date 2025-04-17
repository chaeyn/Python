ans = 0

def f(c):
    global ans

    # 목표 상태
    if c < 1:
        ans += 1
        return

    # 탐색 종료
    if c == 1:
        return

    # 다음 상태
    f(c - 1)
    f(c - 2)
    f(c - 3)

    return 

# 체력 입력
n = int(input())

# 초기 상태
f(n)

# 경우의 수 출력
print(ans)
