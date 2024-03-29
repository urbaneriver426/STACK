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
	
	def balance(self, string):
		for i in range(len(string)):
			if string[i] == "(":
				self.push(string[i])
			elif string[i] == ")":
				if self.size() == 0:
					return "unbalanced"
				else:
					self.pop()
		if self.size() == 0:
			return "balanced"
		else:
			return "unbalanced"
