def maxi(a, b, c):
    if a > b and a > c:
        return 1
    elif b > a and b > c:
        return 2
    else:
        return 3

def mini(a, b, c):
    if a < b and a < c:
        return 1
    elif b < a and b < c:
        return 2
    else:
        return 3

a, b, c = map(int, input().split())
print(maxi(a, b, c), mini(a, b, c))
