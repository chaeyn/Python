arr = [0]

# 1번, 2번, 3번 놀이기구의 요금 저장
charge = [0, 1000, 1200, 2000]

# 가지고 있는 돈과 놀이기구의 수 입력
n, m = map(int, input().split())

# m개의 놀이기구 번호 입력
arr.extend(map(int, input().split()))

def f(now, mon):
    # 현재 사용 요금이 소유한 금액보다 크다면
    # 최종적으로 탑승한 놀이기구 번호 출력
    if mon > n:
        print(arr[now - 1])
        return

    # 모든 놀이기구를 탑승하였다면
    # 마지막 탑승 놀이기구의 번호와 남은 돈을 출력
    if now == m:
        print(arr[-1], n - mon)
        return
    
    f(now + 1, mon + charge[arr[now + 1]])

# 함수 호출
f(0, 0)
