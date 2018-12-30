b = "F"
b2 = "F"
temp = 0
z = 0
max = 0
count = 0
#for loop in range(0,13195):
loop = 600851475143

while(loop > 600851470000):
    loop-=1
    b="T"
    if(loop%2 == 0):
        b = "F"
    if(loop%3 == 0):
        b = "F"
    if((loop%5 == 0)):
        b = "F"
    if(b=="T"):
        temp = loop
        print(temp)
        if(temp > max):
            max = t

print(max)
