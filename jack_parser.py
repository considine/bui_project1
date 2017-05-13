INTEGER, PLUS, EOF, MINUS, ARITH, OPARENS, CPARENS = 'INTEGER', 'PLUS', 'EOF', 'MINUS', ['PLUS', 'MINUS'], "(", ")"

class Stack (object):
	def __init__(self):
		self.l = []
	def push(self, it):
		l = [it]
		self.l = l + self.l
	def pop(self):
		# remove the 0 index
		del self.l[0]
	def printTop(self):
		print self.l[0]

class UnbalancedException(Exception):
    def __init__(self, message, errors):
        super(ValidationError, self).__init__(message)
        # self.errors = errors
class TokenStack(Stack):
	def __init__(self):
		super(TokenStack, self).__init__()
		self.openParens = 0
	def push(self, it):
		if (it.type == "("):
			self.openParens +=1
		elif (it.type == "("):
			self.openParens -=1

		if self.openParens < 0:
			raise UnbalancedException("Error with parentheses!")

		super(TokenStack, self).push(it)
		
	


class Token (object):
	def __init__(self, value, type):
		self.value = value
		self.type = type

	def __str__(self):
		return 'Token({type}, {value})'.format(
				type=self.type,
				value = self.value
			)

	def __repr__(self):
		return self.__str__()

class Interpreter (object):
	def __init__(self, text):
		self.text = text
		self.currentToken = None
		self.pos = 0 

	def error (self):
		raise Exception("Error parsing input")

	def getNextToken(self):
		text = self.text

		if self.pos >= len(text) -1:
			return Token(None, EOF)

		
		cur_char = text[self.pos]
		


		if cur_char.isdigit():
			self.pos+=1
			while self.pos < len(text) and text[self.pos].isdigit():
				cur_char += text[self.pos]
				self.pos+=1	
			return Token(int(cur_char), INTEGER)
		if cur_char == "+":
			self.pos+=1
			return Token(cur_char, PLUS)
		if cur_char == '-':
			self.pos+=1
			return Token(cur_char, MINUS)
		if cur_char == " ":
			self.pos+=1
			return self.getNextToken();
		self.error()
	def expr(self):
		# Get the first token
		self.currentToken = self.getNextToken()
		left = self.currentToken
		self.eat(INTEGER)
		op = self.currentToken
		try:
			self.eat(PLUS)
			right = self.currentToken
			self.eat(INTEGER)
			result = right.value + left.value
			return result
		except: 
			self.eat(MINUS)
			right = self.currentToken
			self.eat(INTEGER)
			result = left.value - right.value
			return result
	def eat (self, token_type):		
		if self.currentToken.type == token_type:
			self.currentToken = self.getNextToken();
		else:
			self.error()
if __name__=="__main__":
	item = TokenStack();
	
	
	v = Token(5, "INTEGER")
	item.push(v)
	item.printTop(	)

	# text="25 + 33"
	# i = Interpreter(text)
	# print i.expr()


	
