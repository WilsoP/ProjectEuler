bool="f"
b="f"
x=99
y=99
while((b=="f") and (x>0)):
    for a in range(0,10):
        for b in range(0,10):
            total=x*y
            total=str(total)
            if((total[1])==(total[4]) and (total[2]==total[3])):
                b="t"
            y-=1
        x-=1

if(b=="t"):
    print(t)
if(b=="f"):
    print(error)
