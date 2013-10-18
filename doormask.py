
allowed=0

door1=1
door2=2
door3=4
door4=8

#Allow access to door 1 and 3

allowed|=door4 
allowed|=door3





print "Allow in d1?",allowed&door1>0
print "Allow in d2?",allowed&door2>0
print "Allow in d3?",allowed&door3>0
print "Allow in d4?",allowed&door4>0

print bin(allowed)
