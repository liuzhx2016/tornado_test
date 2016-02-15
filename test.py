#*-* coding:utf-8 *-*
import os,shutil,re
from string import Template
def compare(a,b):
	return a > b

def Testsort():
	a = [2,423,65,2,54,65,764,35,5363,3,327,6534,325,23,65,4326,62,]
	b = sorted(a,cmp=compare)
	print a
	print b

# 模板化输出字符串
def Testtemp():
	s = Template("$x is a good guy!")
	ss = s.substitute(x = "liuzhx")
	print ss

def main():
	text = "JGood is a handsome boy, he is cool, clever, and so on..."
	m = re.finditer(r" is ", text)
	age = -100
	assert 0 < age < 100 , "the age is out of range"
	for match in m:
		print match.group()
		#print match.len() #可以找到对应的位置
__metaclass__ = type

class Person:
	__name = "" # 这个是类变量，可供类内使用,如果没有双下划线就是共有变量。如果有的话就是私有变量,私有变量无法继承
				#对于方法来说是一样的
				#私有变量是完全隐藏的，在类外是无法访问的，也不可见的
	age = 0
	def setName(self,name):
		self.__name = name
	def setAge(self,age):
		self.age =  age
	def greet(self):
		print "My name is %s , my age is %d" %(self.__name,self.age)

class Student(Person):
	stu_num = 0
	name = ""
	def setNum(self,num):
		self.stu_num = num
	def greet(self):  #重写了定义
		# super().greet(self)
		print "My name is %s , my age is %d,my num is %d" %(self.name,self.age,self.stu_num)

class Teacher(Person):
	def __init__(self,name1):
		self.name = name1
	def greet(self):
		super(Teacher,self).greet() #调用父类的函数,__metaclass__ = type 父类一定要使新类型
		print "My name is %s , my age is %d" %(self.name,self.age)

def function1(*arg, **args):
	print arg
	print args

# 自定义的结构体测试
class Rect:
	def __init_(self):
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
	def __setattr__(self,name,value):
		if name == "size":  # 有点类似于结构体
			self.x , self.y , self.width , self.height = value
		else:
			self.__dict__[name] = value
	def __getattr__(self,name):
		if name == "size":
			return self.x , self.y , self.width , self.height
		else:
			raise error
#使用迭代器
class Fibo:
	def __init__(self):
		self.x1 = 0
		self.x2 = 1
	def next(self):
		self.x1 , self.x2 = self.x2,self.x1 + self.x2 #迭代器的使用
		if self.x1 > 1000 : raise StopIteration
		return self.x1
	def __iter__(self):
		return self

if __name__ == "__main__":
	# main()
	liuzhx = Person()
	liuzhx.setName("liuzhx")
	liuzhx.setAge(24)
	liuzhx.greet()
	# print liuzhx.__name
	
	haha = Student()
	haha.setNum(234)
	haha.greet()

	print hasattr(Person,"age")

	try:
		1.0/0.0
	except Exception,e:
		print e
		print "error!"
	finally:
		print "continue doing the program"

	ll = Teacher("fdsafd")
	ll.greet()

	function1(12,31,42,5437,64756,87865,7643,64,ab=12,fd=23,df="fdsa") #收集参数

	buf = [123,4325,364,4356,452,136,32532,65,326,235,23,452,3]
	print "the len is:" + str(buf.__len__())

	rect = Rect()
	rect.size = [1,4,5643,634]
	print rect.size
	print rect.y

	fibs = Fibo()
	print list(fibs)

	def flat(input):
		yield input[1]

	def conflic(prince,nextX):
		prince_num = len(prince)
		for p_line in range(prince_num):
			if abs(prince[p_line] - nextX ) in (0,prince_num - p_line) :  #可以判断横竖和斜向的
				print "have conflic",prince[p_line]
				return True
		return False

	def queens(num, state = ()):
		for pos in range(num):
			if not conflic(state,pos):
				if len(state) == num - 1:
					yield (pos,)
				else:
					for result in queens(num,state + (pos,)):
						yield (pos,) + result
	
	#fmdskalfndsak

	#fdsagf

	#nf;sdjakgfgsajdf

	#fjsafkg;hjsak;
	print (queens(4))
