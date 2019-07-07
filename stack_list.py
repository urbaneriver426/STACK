class Stack:
	def __init__(self):
		self.stack = []

	def size(self):
		return len(self.stack)

	def pop(self):
		if self.size() != 0:
			self.peek()
			return self.stack.pop()
		else:
			return None

	def push(self, value):
		self.stack.append(value)
	

	def peek(self):
		if self.size() != 0:
			return self.stack[self.size()-1]
		else:
			return None
	
	def balance(self):
		if self.peek() != ")":
			return "unbalanced"
		else:
			count = 0
			for i in range(self.size()):
				x = self.pop()
				if x == ")":
					count += 1
				elif x == "(":
					count -= 1
			if count == 0:
				return "balanced"
			else:
				return "unbalanced"
