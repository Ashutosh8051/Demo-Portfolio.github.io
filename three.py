x1= int(input("Enter x1 "))
y1= int(input("Enter y1 "))
x2= int(input("Enter y2 "))
y2= int(input("Enter y2 "))

#calculating dy and dx 
dy=y2-y1
dx=x2-x1

#calculaing the step
if(dy>dx):
    step=dy
else:
    step=dx

#calcutaing the value of m 
m = dy/dx 
print((x1+(float)(1/m)))
print(m)
if(m>1):
    print(x1 , y1)
    for i in range (step):
        x1=(round)((float)((x1+(float)(1/m))))
        y1= round(y1+1)
        print(x1 , y1)

elif(m==1):
     print(x1 , y1)
     for i in range (step):
        x1=(round)(x1+1)
        y1= round(y1+1)
        print(x1 , y1)
else:
    print(x1 , y1)
    for i in range (step):
        x1=(round)(x1+1)
        y1= round(y1+float(m))
        print(x1 , y1)