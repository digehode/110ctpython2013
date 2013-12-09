class Shape(object):
    def __init__(self):
        self.contents=[]
    def display(self):
        out=""
        for y in range(20):
            for x in range(20):
                if (x,y) in self.contents:
                    out+="#"
                else:
                    out+=" "
            out+="\n"
        print out

class Square(Shape):
    def __init__(self,location, size):
        Shape.__init__(self)
        for y in range(size):
            for x in range(size):
                self.contents.append( (x+location[0],y+location[1]))
    
a=Square((5,1),8)
a.display()
        
