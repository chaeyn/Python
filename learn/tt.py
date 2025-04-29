m = []
for i in range(4):
    row = input().split()
    row = [int(x) for x in row]
    m.append(row)

ravg = []
for row in m:
    ravg.append(sum(row) // len(row))

cavg = []
for j in range(2):
    csum = 0
    count = 0
    for i in range(4):
        if j < len(m[i]):
            csum += m[i][j]
            count += 1
    cavg.append(csum // count)

tsum = 0
tcount = 0
for row in m:
    tsum += sum(row)
    tcount += len(row)
avg = tsum // tcount

print(*ravg)
print(" ".join(map(str, cavg)))
print(avg)