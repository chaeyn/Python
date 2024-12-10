c, s, l = map(int, input().split())
result = float(c*s*l/8/1024/1024)
print("%.2f MB" %(result))