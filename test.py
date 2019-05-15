class MyClass:
    i = 23423
    def f(self):
        return 'hello world'
x = MyClass()
print('MyClass 类的属性 i 为： ', x.i)
print('MyClass 类的方法 f的输出为：', x.f())
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, 4.5)
print(x.r, x.i)

class fullname:
    def __init__(self, first, last):
        self.first = first
        self.last = last
name1 = fullname('y.h', 'huang')
print(name1.first, name1.last)

name2 = fullname('z.h', 'lin')
print(name2.first, name2.last)


import numpy as np
a = [['55.0D0', '15.0D0'], ['55.0D0', '5.0D0'], ['55.0D0', '15.0D0']]
aa = np.reshape(a, (2, 3))
b = ['55.0D0', '55.0D0', '45.0D0']
bb = np.array(b).reshape(1, len(b))
l = np.concatenate((aa, bb), axis = 0)
print(l)
#把二维数组转换成一维数组
ll = l.flatten()
print(ll)
