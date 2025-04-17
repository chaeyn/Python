def f(c, a, b):
    if a > c or b > c:  # 화살이 과녁 밖에 있으면
        return 0
    elif a == b:  # 화살의 세로 가로 좌표가 같으면
        return a + b
    elif a > b:  # 세로 좌표가 크면
        return a
    else:  # 가로 좌표가 크면
        return b

# 과녁의 크기와 화살의 수 입력
n, m = map(int, input().split())
ans = 0
for i in range(m):
    # m개의 화살의 좌표 입력
    a, b = map(int, input().split())
    # 점수를 계산하는 함수 호출 및 점수 누적
    ans += f(n, a, b)
# 최종 
