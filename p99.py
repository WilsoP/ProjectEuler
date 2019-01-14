max = 0
maxc = 0
counter = 0
with open("p99txt.txt","r") as f:
    for line in f:
        current = line.split(",")
        n = int(current[0])**int(current[1])
        counter += 1
        if len(str(n)) == len(str(max)):
            if n > max:
                max = n
                maxc = counter
        elif len(str(n)) > len(str(max)):
            max=n
            maxc = counter
print(max)
print(maxc)
