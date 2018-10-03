b = "F"
b2 = "F"
temp = 0
z = 0
max = 0
count = 0
#for loop in range(0,13195):
loop = 600800000000 

while(loop < 600851475143):
    loop+=1
    b="T"
    if((loop != 2 ) and (loop%2 == 0)):
        b = "F"
    x = 0
    y = 0
    z = 0
    x=len(str(loop))
    for i in range (0,(x-1)):
        y=str(loop)[i]
        z+=int(y)
    if (z%3 == 0):
        b2="T"
        #print(b2)
    if((loop != 3) and (b2=="T")):
        b = "F"
        #print(loop)
    if((loop != 5) and (loop%5 == 0)):
        b = "F"
    if(b=="T"):
        temp = loop
        print(temp)
        if(temp > max):
            max = temp

print(max)
