import matplotlib.pyplot as plt


    
plt.axes()
line=plt.Line2D((2,8),(6,7), lw=1.5)
plt.gca().add_line(line)
line=plt.Line2D((4,18),(16,17), lw=1.5)
plt.gca().add_line(line)
plt.axis('scaled')
plt.show()

class prostokat():
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.bokA=b[0]-a[0]
        self.bokB=d[1]-a[1]
    
    def boki(self):
        return [self.bokA, self.bokB]
    
    def pole(self):
        return self.bokA*self.bokB
    
    def obwod(self):
        return 2*self.bokA + 2*self.bokB
    
    def rysuj(self):
        plt.axes()
        line=plt.Line2D((self.a[0], self.a[1]), (self.b[0], self.b[1]),lw=1.5)
        plt.gca().add_line(line)
        line=plt.Line2D((self.b[0], self.b[1]), (self.c[0], self.c[1]),lw=1.5)
        plt.gca().add_line(line)
        line=plt.Line2D((self.c[0], self.c[1]), (self.d[0], self.d[1]),lw=1.5)
        plt.gca().add_line(line)
        line=plt.Line2D((self.d[0], self.d[1]), (self.a[0], self.a[1]),lw=1.5)
        plt.gca().add_line(line)
        plt.axis('scaled')
        plt.show
        
class prostyprostokat():
    def __int__(self,a,b):
        self.a=a
        self.b=b
        
    def obwod(self):
        return self.a*self.b
    
    def pole(self):
        return self.a*self.b
    
class prostykwadrat:
    def __init__(self,a):
        super().__init__(a,a)