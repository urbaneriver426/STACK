	def postfix(self, string):
		new_stack = Stack()
		x = ""
		for i in range(len(string)-1,-1,-1):
			if string[i] == " ": 
				self.push(x)
				x = ""
			elif i == 0:
				x = string[i] + x
				self.push(x)
			elif string[i] != " ":
				x = string[i] + x

		for i in range(self.size()):
			z = self.pop()
			if z == "+":
				x = int(new_stack.pop())
				y = int(new_stack.pop())
				new_stack.push(x+y)
			elif z == "*":
				x = int(new_stack.pop())
				y = int(new_stack.pop())
				new_stack.push(x*y)
			elif z == "=":
				return new_stack.pop()
			else:
				new_stack.push(z)
