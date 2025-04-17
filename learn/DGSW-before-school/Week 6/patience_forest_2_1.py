ans = 0

def f(c):
    global ans

    # 목표 상태: 체력이 1일 때만 카운트
    if c == 1:
        ans += 1
        return

    # 탐색 종료: 체력이 1 미만이면 더 이상 진행하지 않음
    if c < 1:
        return

    # 다음 상태
    f(c - 1)  # 1 감소
    f(c - 2)  # 2 감소
    f(c - 3)  # 3 감소

# 체력 입력
n = int(input())

# 초기 상태
f(n)