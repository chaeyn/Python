arr = []

for i in range(12):
  arr.append([])
  for j in range(12):
    arr[i].append(0)
for i in range(10):
  a = input().split()
  for j in range(10):  
    arr[i+1][j+1]=int(a[j])
    
x, y = 2, 2

while True:
    if arr[x][y] == 0:
        arr[x][y] = 9
    elif arr[x][y] == 2:
        arr[x][y] = 9
        break
    
    if (arr[x][y+1] == 1 and arr[x+1][y] == 1) or (x == 9 and y == 9):
        break
    if arr[x][y+1] != 1:
        y += 1
    elif arr[x+1][y] != 1:
        x += 1
        
for i in range(1, 11):
    for j in range(1, 11):
        print(arr[i][j], end=' ')
    print()