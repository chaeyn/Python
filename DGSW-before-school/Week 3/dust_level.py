n = int(input())
if 0 <= n <= 30:
    print("Good")
elif 31 <= n <= 80:
    print("Moderate")
elif 81 <= n <= 150:
    print("Unhealthy")
else:
    print("Very Unhealthy")
