x=int(input("enter first value"))
y=int(input("enter second value"))
z=int(input("enter second value"))
if(x>y and y>z):
    print("x is greatest")
elif(x>z and z>y):
   print("x is greatest")
elif(y>x and x>z):
   print("y is greatest")
elif(y>z and z>x):
   print("y is greatest")
elif(z>x and x>y):
   print("z is greatest")
else:
       print("z is greatest")