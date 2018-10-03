x = 1
y = 1
i = 0
t = 0
while (i < 4000000):
#for j in range(0,10):
    i = x + y
    x = y
    y = i
    print(i)
    if ((i%2) == 0):
        t+=i

print(t)
