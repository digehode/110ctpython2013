import random

def makeUniverse(l):
    output=[1]
    for i in range(l-2):
        if random.randint(0,1) == 1:
            output+=[1]
        else:
            output+=[0]
    return output+[1]

def display(u):
    
    out=""
    for i in u:
        if i==1: out+="@"
        else: out+=" "
    return out

def step(u):
    out=[1]
    for i in range(1,len(u)-1):
        count=sum(u[i-1:i+2])
        if 0<count<3:
            out+=[1]
        else:
            out+=[0]
    return out+[1]


universe=makeUniverse(140)
print display(universe )
for i in range(100):
    universe=step(universe)
    print display(universe )
