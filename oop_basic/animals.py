#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running')

class Dog(Animal):
	pass
#	def run(self):
#		print('Dog is running')

class Cat(Animal):
	def run(self):
		print('Cat is running')
		
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
        
class Timer(object):
    def run(self):
        print('Timer start...')

#传入的参数并不是一定要是Animal类型，只要该类型包含run方法就可以
def run_twice(animal):
	animal.run()
	animal.run()
	
a = Animal()
b = Dog()
c = Cat()
d = Tortoise()
e = Timer()

print('a is Animal?',isinstance(a,Animal))
print('b is Dog?',isinstance(b,Dog))
print('c is Cat?', isinstance(c, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

#Dog 继承了Animal中的run方法
b.run()
#Cat 继承了Animal中的run方法，自己定义的run方法覆盖了继承的，多态
c.run()
#Tortoise 是Animal类型，包含run方法
run_twice(d)
#Timer中也有run方法，就可以作为run_twice的参数
run_twice(e)


