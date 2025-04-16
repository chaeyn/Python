w = input()
num_2 = "ABC"; num_3 = "DEF"; num_4 = "GHI"; num_5 = "JKL"
num_6 = "MNO"; num_7 = "PQRS"; num_8 = "TUV"; num_9 = "WXYZ"
time = 0
for i in range(len(list(w))):
    if w[i] in num_2:
        time += 3
    elif w[i] in num_3:
        time += 4
    elif w[i] in num_4:
        time += 5
    elif w[i] in num_5:
        time += 6
    elif w[i] in num_6:
        time += 7
    elif w[i] in num_7:
        time += 8
    elif w[i] in num_8:
        time += 9
    elif w[i] in num_9:
        time += 10
print(time)