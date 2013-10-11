#Find an x,y coordinate on a screen from a counter value (pos)
pos = 60
w =30
h = 30

x=pos%w
y=pos//w
 
print pos,"is at position (",x,",",y,")"
