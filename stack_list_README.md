Стек на основе list.  Реализация методов pop(), push() и peek().

1)	Метод pop(). Проверяем размер стека, если он не равен нулю, используем встроенный метод списка pop(). В противном случае метод возвращает None:

def pop(self):
		if self.size() != 0:
			self.peek()
			return self.stack.pop()
		else:
			return None

2)	Метод push().  Используем встроенный метод списка append():

def push(self, value):
		self.stack.append(value)

3)	 Метод peek().  Проверяем размер стека, если он не равен нулю, возвращаем объект списка. В противном случае метод возвращает None:

def peek(self):
		if self.size() != 0:
			return self.stack[self.size()-1]
		else:
			return None
