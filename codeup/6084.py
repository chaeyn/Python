h, b, c, s = map(int, input().split())
result = float((h*b*c*s/8)/1024/1024)
print("%.1f MB" %(result))