def triangles():
    N=[1]
    while True:
        yield N
        N=[1]+[N[i]+N[i+1] for i in range(len(N)-1)]+[1]

for x in triangles():
    print(x)