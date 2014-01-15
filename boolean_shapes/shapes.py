
def distance (p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5


class Shape(object):
    def __init__(self):
        self.contents=[]
        self.centroid=None
    def calculateCentroid(self):
        x=0.0
        y=0.0
        for i in self.contents:
            x+=i[0]
            y+=i[1]
        self.centroid=(int(x/len(self.contents)),int(y/len(self.contents)))
    def display(self):
        self.calculateCentroid()
        out=""
        for y in range(40):
            for x in range(40):
                if (x,y)==self.centroid:
                    out+="@"
                elif (x,y) in self.contents:
                    out+="#"
                else:
                    out+="."
            out+="\n"
        print out
    def subtract(self,shape):
        newShape=Shape()
        for i in self.contents:
            if not i in shape.contents:
                newShape.contents.append(i)
        return newShape
    def xor(self,shape):
        newShape=Shape()
        for i in self.contents + shape.contents:
            if (i in shape.contents or i in self.contents) and not (i in shape.contents and i in self.contents):
                newShape.contents.append(i)
        return newShape
    def add(self,shape):
        newShape=Shape()
        for i in self.contents:
            newShape.contents.append(i)
        for i in shape.contents:
            if i not in newShape.contents:
                newShape.contents.append(i)
        return newShape
    def __add__(self,other):
        return self.add(other)
    def __sub__(self,other):
        return self.subtract(other)
    def __or__(self,other):
        return self.add(other)
    
class Triangle(Shape):
    def __init__(self,location,size):
        Shape.__init__(self)
        for i in range(size):
            for j in range(i+1):
                self.contents.append((location[0]+j,location[1]+i))
        
    
class Square(Shape):
    def __init__(self,location, size):
        Shape.__init__(self)
        for y in range(size):
            for x in range(size):
                self.contents.append( (x+location[0],y+location[1]))

class Circle(Shape):
    def __init__(self,location,r):
        Shape.__init__(self)
        for x in range(2*r):
            for y in range(2*r):
                xp=x+location[0]-r
                yp=y+location[1]-r
                if distance(location,(xp,yp))<=r:
                    self.contents.append((xp,yp))


myCircle=Circle((15,15),10)
a=Square((5,1),14)
t=Triangle((6,2),12)
(a-t).display()


                    
##(myCircle-a+Circle((10,10),5)).display()



        
