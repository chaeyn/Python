# 공격력, 행운, 힘, 민첩, 지력, 체력, 마나
At, Lu, St, Ag, In, Sm, Ma = 0, 0, 0, 0, 0, 0, 0
S = [0] * 10

def f(c):
    global At, Lu, St, Ag, In, Sm, Ma
    if c == 1:  # 주문서 1인 경우
        At += 5
        Lu += 5
        Sm += 10
    elif c == 2:  # 주문서 2인 경우
        At += 1
        Ag += 2
        Lu += 2
    elif c == 3:  # 주문서 3인 경우
        At += 10
        St += 10
        Lu += 10
    else:  # 주문서 4인 경우
        At += 7
        In += 10
        Ma += 10
        Sm += 10

# 초깃값 공격력, 행운, 힘, 민첩, 지력, 체력, 마나 입력
At, Lu, St, Ag, In, Sm, Ma = map(int, input().split())
i = list(map(int, input().split()))
for k in i:
    f(k)

# 최종 공격력, 행운, 힘, 민첩, 지력, 체력, 마나 출력
print(At, Lu, St, Ag, In, Sm, Ma)
