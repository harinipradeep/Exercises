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


x = DoAdd(10)
y = DoMul(10)
print(x.do_operation())
print(y.do_operation())

#$ python abstractclass.py 
#20
#100
