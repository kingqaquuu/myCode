from math import sqrt
class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def move_to(self,x,y):
        self.x=x
        self.y=y
    def move_by(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def distance(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        return sqrt(dx**2+dy**2)
    def _show(self):
        return '(%s,%s)' % (str(self.x),str(self.y))
def main():
    p1=Point(2,3)
    p2=Point()
    print(p1)
    print(p2)
    p1.move_by(1,1)
    print(p1)
    print(p2.distance(p1))
if __name__ == '__main__':
    main()