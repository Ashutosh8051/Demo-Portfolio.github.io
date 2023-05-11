from graphics import *
x1= int(input("Enter x1 "))
y1= int(input("Enter x2 "))
x2= int(input("Enter y1 "))
y2= int(input("Enter y2 "))

#calulating the dy and dx
dy=y2-y1
dx=x2-x1 


#calculating the steps 
if(dy>dx):
    step=dy
else:
    step=dx

# caluclating the slope 
m= dy/dx
win =GraphWin()
#case 1 if m >=1
if(m>=1):
    pk=((2*dx)-dy)
   
    print(x1, y1)
    for i in range (step):
        if(pk>=0):
            x1=x1+1
            y1=y1+1
            print(x1, y1)
            p=Point(x1,y1)
            p.draw(win)
            pk=pk+(2*dx-2*dy)
        else:
            x1=x1

            y1=y1+1
            print(x1, y1)
            p=Point(x1,y1)
            p.draw(win)
            pk=pk+2*dx
else:
    pk=((2*dy)-dx)
    print(x1, y1)
    for i in range (step):
        if(pk>=1):
            x1=x1+1
            y1=y1+1
            print(x1, y1)
            pk=pk+2*dy-2*dx
        else:
            x1=x1+1
            y1=y1
            print(x1, y1)
            pk=pk+2*dy
win.getMouse()
 


# case 2 if m<1