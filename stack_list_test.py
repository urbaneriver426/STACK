import unittest
class TestStack(unittest.TestCase):
	def setUp(self):
		self.stack = Stack()

	def testSizeEmpty(self):
		assert self.stack.size() == 0

	def testPopEmpty(self):
		x = self.stack.pop()
		assert x is None

	def testPeekEmpty(self):
		x = self.stack.peek()
		assert x is None

	def testPushOne(self):
		self.stack.push(1)
		if self.stack.stack[0] == 1:
			x = self.stack.peek()
			assert x == 1
			self.stack.size() == 1
 
	def testPushThree(self):
		for i in range(3):
			self.stack.push(i)
			assert self.stack.stack[i] == i
			x = self.stack.peek()
			assert x == i
		assert self.stack.size() == 3

	def testPopThree(self):
		for i in range(3):
			self.stack.push(i)
		self.stack.pop()
		x = self.stack.peek()
		assert x == 1
		assert self.stack.size() == 2



if __name__ == '__main__':
	unittest.main()
