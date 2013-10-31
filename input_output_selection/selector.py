import random
d1=random.randint(1,6)
d2=random.randint(1,6)
print "D1: %d\nD2: %d"%(d1,d2)
if d1>=4:
    print "First roll is good..."
    if d2<=3:
        print "And so is the second! Wooo!"
    else:
        print "Second roll is a fail. Sad face."
else:
    print "Failed the first hurdle."
    if d2<=3:
        print "And the second roll was a good one, too. Sucks to be you."
    else:
        print "And the second. You are the worst dice roller ever."
