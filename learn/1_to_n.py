def repeat(n):
    if n == 1:
        return 1
    if n >= 2:
        n = n + repeat(n-1)
        return n
print(repeat(1))