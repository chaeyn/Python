n = int(input())
count = 0
def prime(n):
	count = 0
	result = []
	for i in range(1, n+1):
		if n % i ==0:
			count += 1
			result.append(i)
	if count == 2:
		return "wrong number"
	elif count == 4:
		return result[1],result[2]
	elif count > 4:
		return 'wrong number'
a = prime(n)
if type(a)==tuple:
	print(*a)
else:
  print(a)
