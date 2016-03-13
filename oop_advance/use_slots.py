#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
print(s.name)
print(s.age)

# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

from types import MethodType

def set_score(self, score): 
	self.score = score
	
def set_age(self, age):
	self.age = age
	
def set_name(self, name):
	self.name = name
	
	
try:
    s.set_score = MethodType(set_score, s) 
except AttributeError as e:
    print('AttributeError:', e)



g1 = GraduateStudent()
g2 = GraduateStudent()

g1.score = 92
print('g1.score =', g1.score)

g1.set_age = MethodType(set_age,g1)
g1.set_age(23)
print('g1.age = ',g1.age)

try:
    g2.set_age(24) 
except AttributeError as e:
    print('AttributeError:', e)
    
GraduateStudent.set_name = MethodType(set_name,GraduateStudent)
g1.set_name('bob')
print('g1.name = ',g1.name)
g2.set_name('jack')
print('g2.name = ',g2.name)












