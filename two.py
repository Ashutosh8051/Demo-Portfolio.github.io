from graphics import *
x1=int(input("x1"))
y1=int(input("y1"))
x2=int(input("x2"))
y2=int(input("y2"))

# calculating dy and dx
dy=y2-y1
dx=x2-x1

#calculating the steps 
if(dy>dx):
    step=dy
else:
    step=dx

#calculating m 
m = dy/dx
Win=GraphWin()
if(m>1):
    D_initial=((2*dx)-dy)
    D=2*(dx-dy)
    if(D_initial>=0):
        D_initial=D_initial+D
       
        y1=y1+1
        x1=x1+1
        print(x1, y1)
        p=Point(x1,y1)
        p.draw(Win)

    else:
         D_initial=(D_initial+(2*dx))
        
         y1=y1+1
         x1=x1
         print(x1, y1)
         p=Point(x1,y1)
         p.draw(Win)

else:
     D_initial=((2*dy)-dx)
     D= 2*(dy-dx)
     for i in range (step):
        if(D_initial>=0):
            D_initial=D_initial+D
            
            x1=x1+1
            y1=y1+1
            print(x1,  y1)
            p=Point(x1,y1)
            p.draw(Win)
        else:
            D_initial=D_initial+2*dy
           
            x1=x1+1
            y1=y1
            print(x1,  y1)
            p=Point(x1,y1)
            p.draw(Win)
Win.getMouse()