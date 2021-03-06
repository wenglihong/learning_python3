#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

#导入其他文件要注意的地方，如果只导入文件名，则用该文件里的类时都要在其前面加上模块名作为限定
#还可以直接导入类，这样就不用加限定空间了
import animals
from animals import Dog

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))
print('type(\'abc\')==str?', type('abc')==str)

a = animals.Animal()

class Husky(Dog):
	pass

#使用isinstance()判定类型
h = Husky()
print('h is Husky ',isinstance(h,Husky))
print('h is Dog ',isinstance(h,Dog))
print('h is Animal ',isinstance(h,animals.Animal))


print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))






