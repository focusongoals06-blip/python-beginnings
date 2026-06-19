#Variable and datatypes
x = 5
y = "Rocky"
print (x , y)
fruits = ["Orange","Banana","Apple"]
x1,y1,z1=fruits
print(x1)
print(y1)
print(z1)
a=b=c="Hello"
print(a)
print(b)
print(c)
a1=5
b1="Hello"
c1=60.0
d1=True
print(type(a1))
print(type(b1))
print(type(c1))
print(type(d1))
#local variable

e = "Hii"

def east():
    e = "Bye"

east()
print(e)
#global variable

d = "Hii"

def best():
    global d
    d = "Bye"

best()
print(d)
