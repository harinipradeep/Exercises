from abc import ABCMeta, abstractmethod
class Operations(object):
	__metaclass__ = ABCMeta

	def __init__(self, value):
		self.value = value

	@abstractmethod
	def do_operation(self):
		pass

class DoAdd(Operations):
	def do_operation(self):
		return self.value + 10

class DoMul(Operations):
	def do_operation(self):
		return self.value * 10

class DoNone(Operations):
	def add(self):
		pass


x = DoAdd(10)
y = DoMul(10)
z = DoNone(10)
print(x.do_operation())
print(y.do_operation())

#$ python abstractclass.py 
#Traceback (most recent call last):
#  File "abstractclass.py", line 27, in <module>
#    z = DoNone(10)
#TypeError: Can't instantiate abstract class DoNone with abstract methods do_operation

#O/p When we have not instantiated DoNone class
#$ python abstractclass.py 
#20
#100
