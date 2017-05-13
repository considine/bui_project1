from abc import ABCMeta, abstractmethod


class ArithmeticExpr:
	""" Do not call upon this class"""	
	def __init__(self):
		raise Exception("Instantiating a baseclass")
	def calc(self):
		return self.result



class AdditionExpr(ArithmeticExpr):
	def __init__(self, arg1, arg2):
		self.result = arg1 + arg2
	# def calc(self):
	# 	return self.result
class MultiplicationExpr (ArithmeticExpr):
	def __init__(self, arg1, arg2):
		self.result = arg1 * arg2

class DivisionExpr (ArithmeticExpr):
	def __init__(self, arg1, arg2):
		self.result = float(arg1) / float(arg2)

class SubtractionExpr (ArithmeticExpr):
	def __init__(self, arg1, arg2):
		self.result = arg1 - arg2

class ExpressionFactory(object):
	def __init__(self, opcode, **kargs):
		
		# opcodemap = {
		# 	"+" : AdditionExpr(),
		# 	"-" : SubtractionExpr(),
		# 	"*" : MultiplicationExpr(),
		# 	"/" : DivisionExpr()
		# }
		self.expr = opcodemap[opcode]
	def getExpr(self):
		return self.expr

class ParserStack(object):
	def __init__(self):
		self.l = []
	def push(self, item):
		self.l = [item] + self.l
		# print len(self.l)
	def pop(self):
		if len(self.l) == 0:
			raise PopError('Trying to pop empty stack!')
		t = self.l[0]
		self.l = self.l[1:len(self.l)]

	def getTop (self):
		""" Without popping, just return the top"""
		if len(self.l) == 0:
			raise PopError('Trying to reference top of empty stack!')
		return self.l[0]



class ExpressionStack (ParserStack):
	"""class for pushing expressiosn to a stack
	as they are being parsed. Includes a 'write """
	def __init__(self):
		super(ParserStack, self).__init__()



class PopError(IndexError):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(IndexError, self).__init__(message)

class ParseError(SyntaxError):
	def __init__(self, message):
		super(SyntaxError, self).__init__(message)


#Need some sort of pointer with expressions


# Every time we get a new open parens, we have a new expression
#  Want: Push new parens, open new expr, maybe expression list of strings?
#   

class Interpreter(object):
	def __init__(self, text):
		self.parensStack = ParserStack()
		self.index=0
		self.openParens = 0
		self.expressionList = []
		self.text = text;

	# def getOp (self):
	# 	"""Get first non space symbol after the new parens"""
	# 	self.index+=1
	# 	char = self.text[self.index]
	# 	while (char == ' '):
	# 		self.index+=1
	# 		char = self.text[self.index]
	# 	opstring = ''

	# 	#delimited by space: keep going until we hit the space
	# 	while (char != ' '):
	# 		opstring += char
	# 		self.index+=1
	# 		char = self.text[self.index]

	# 	return opstring


	def readChar(self, char):
		if (char == "("):
			self.openParens +=1
			op = self.getOp()

			
			# Get operation



		else:
			if self.openParens < 1:
				raise ParseError("Misplaced closing parentheses. None open at this point!")
			if char == ")":
				self.openParens -=1
		


		self.parensStack.push(char)
	def interpret(self):
		while (self.index < len(self.text)):
			self.readChar(self.text[self.index])
			self.index+=1
			# push to stack

class Operator(object):
	pass
class Expr (object):
	pass


if __name__ == '__main__':
	interpreter = Interpreter("(+ 5 3)")
	interpreter.interpret()

	interpreter = Interpreter("( * 5 3)")
	interpreter.interpret()

	interpreter = Interpreter("( -= 5 3)")
	interpreter.interpret()





