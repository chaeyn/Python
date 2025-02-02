num = int(input())
if num < 100000 or num > 999999:
    print("6개의 숫자만 입력 가능")
res1 = (num % 10) + (((num % 100) - (num % 10))//10) + (((num % 1000) - (num % 100))//100)
res2 = (((num % 10000) - (num % 1000))//1000) + (((num % 100000) - (num % 10000))//10000) + (((num % 1000000) - (num % 100000))//100000)
if  res1 == res2:
    print(f'{num}:LUCKY')
else:
    print("READY")