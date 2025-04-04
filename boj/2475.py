"""
백준 2475번 검증수

컴퓨터를 제조하는 회사인 KOI 전자에서는 제조하는 컴퓨터마다 6자리의 고유번호를 매긴다. 고유번호의 처음 5자리에는 00000부터 99999까지의 수 중 하나가 주어지며 6번째 자리에는 검증수가 들어간다. 검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.

예를 들어 고유번호의 처음 5자리의 숫자들이 04256이면, 각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81 을 10으로 나눈 나머지인 1이 검증수이다.

입력
첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.

출력
첫째 줄에 검증수를 출력한다.
"""

a = []
a = list(map(int, input().split())) #고유번호 5자리를 1자리씩 나눠 a에 저장

a1 = int(a[0]*a[0]) # 각 자리수를 제곱
a2 = int(a[1]*a[1])
a3 = int(a[2]*a[2])
a4 = int(a[3]*a[3])
a5 = int(a[4]*a[4])

sum = a1 + a2 + a3 + a4 + a5

result = int(sum%10) #결과 계산

print(result)