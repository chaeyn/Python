# 자연수 n이 주어질 때, n개의 줄에 *로 X 모양을 출력하는 프로그램을 작성해보자. n은 항상 홀수이다.
# n이 5이라면 다음과 같이 출력된다.
'''
*   *
 * * 
  *  
 * * 
*   *

1 5
2 4
3 3
4 2
5 1
'''
n = int(input())
for i in range(n):
    for j in range(n):
        if i == j or i + j == n-1:
            print("*", end='')
        else:
            print(" ", end='')
    print()