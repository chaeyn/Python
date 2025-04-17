N = int(input())
Queue = [i+1 for i in range(N)]
f = 0
e = N-1
def deQueue():
    f += 1
    if f >= N:
        f = 0
        return
    Queue[f] = 0
def changeQueue():
    e = f