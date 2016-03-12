#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	
	def print_score(self):
		print('%s,%s' %(self.__name,self.__score))
		
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
			
	def get_name(self):
		return self.__name
	
	def get_score(self):
		return self.__score
		
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

#直接访问私有变量将会出错			
#bart = Student('Bart Simpson',98)
#print(bart.__name)

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)






