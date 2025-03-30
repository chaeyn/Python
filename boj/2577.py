A = int(input())
B = int(input())
C = int(input())
ABC = list(map(int, str(A*B*C)))
lst = []
res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, 10):
    lst.append(i)
for i in range(1, 10):
    for j in range(len(ABC)):
        if i == ABC[j]:
            lst[i] += 1
for i in range(9):
    if ABC[i] == lst[i]:
        res[i] += 1
print(res)