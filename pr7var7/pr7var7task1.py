import math
print ('Введите стороны четырехугольника')
x = float(input('x : '))
y = float(input('y : '))
z = float(input('z : '))
t = float(input('t : '))
d = math.sqrt(x*x+y*y)
def Square1(x, y):
     return x*y*0.5
def Square2(d, z, t):
     p = (z+t+d) / 2
     return math.sqrt(p*(p-z)*(p-t)*(p-d))
print('Площадь ',Square1(x,y) + Square2(d,z,t))