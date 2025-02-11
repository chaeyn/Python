# 수학의 수열의 점화식
# 이웃한 항의 관계를 통해 수열을 나타내는 것
# 팩토리얼 점화식
# 1! = 1
# n이 2이상의 수일 때 ) n! = n * (n-1)!

def factorial(n):
    # 1! = 1
    if n == 1:
        return 1
    # n이 2이상의 수일 때 ) n! = n * (n-1)!
    elif n >= 2:
        return n * factorial(n - 1)
    
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

# f(5)를 실행한다면, 
# f(5) = 5 * f(4)
# f(4) = 4 * f(3)
# f(3) = 3 * f(2)
# f(2) = 2 * f(1)
# f(1) = 1
# f(1) = 1부터 다시 위로 올라가면,
# 2*1, 3*2, 4*6, 5*24 
# ∴ f(5) = 120