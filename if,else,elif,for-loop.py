#If
#if something is true
num = 7
if num > 0:
    print("the munber is positiv.")
    
#Else
#if something is true but Otherwise
num = -3
if num > 0:
    print("the number is positiv")
else:
    print("the number is negativ")
    
#Elif
#om annat villkor ar sant
num = -3
if num > 0:
    print("the number is positiv")
elif num == 0:
    print("the namber is Zero")
else:
    print("the number is negativ")
    
#For-loopar:
#to get 100st hello world
for i in range(1,100,1):
    print("Hello world")
    
#to start from 0 to 100(by one)
#to start fron 1 to 100(1,101,1)
for i in range(0,101,1):
    print("number: " + str(i))
    
#to start  from 1 to 100
for i in range(0,100,1):
    print("number: " + str(i+1))
    
#to start from 0 to 100(by 10)
for num in range(0,101,10):
    print("inside loop, iteration number: " + str(num))