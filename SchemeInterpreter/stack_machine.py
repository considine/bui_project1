from abc import ABCMeta, abstractmethod
import re

class ListExpr:
	pass


class ArithmeticExpr:
	""" Do not call upon this class"""	
	def __init__(self):
		raise Exception("Instantiating a baseclass")
	def calc(self):
		return self.result

class Utility(object):
	def __init__(self):
		pass
	def isNumber(self, s):
		try:
			float(s)
			return True
		except ValueError:
			return False

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

class ArithmeticExpressionFactory(object):
	def __init__(self, opcode, kargs):
		# print kargs
		opcodemap = {
			"+" : AdditionExpr(float(kargs[0]), float(kargs[1])).result,
			"-" : SubtractionExpr(float(kargs[0]), float(kargs[1])).result,
			"*" : MultiplicationExpr(float(kargs[0]), float(kargs[1])).result,
			"/" : DivisionExpr(float(kargs[0]), float(kargs[1])).result

		}
		if opcode not in opcodemap:
			raise UknownOpCodeError("Operation symbol: " + opcode + " not found")
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
class UknownOpCodeError(ParseError):
	def __init__(self, message):
		super(ParseError, self).__init__(message)


#Need some sort of pointer with expressions


# Every time we get a new open parens, we have a new expression
#  Want: Push new parens, open new expr, maybe expression list of strings?
#   

class Interpreter(object):
	def __init__(self, text):
		self.parensStack = ParserStack()
		self.index=0
		self.numOpenParens = 0
		self.expressionList = []
		self.text = text;

	def getChar (self):
		if self.index >= len (self.text):
			raise ParseError("Missing closing parentheses")

		char = self.text[self.index]
		self.index+=1
		return char
	
	def interpret(self):
		self.getOpening()
		self.openParens()
		expr = self.getExpr(self.numOpenParens -1) 
		print expr

	def getExpr(self, stackCount):
		inner = ''
		while self.numOpenParens != stackCount:
			nchar = self.getChar();
			if (nchar == ")"):
				self.closeParens()
			elif (nchar == "("):
				self.openParens()
				nchar = str(self.getExpr(self.numOpenParens - 1)) + " "
				
				
			inner += str(nchar)
		# return inner[0:len(inner)-1]
		if (len(inner) == 1):
			return ""
		ret = self.evalExpr(inner[0:len(inner)-1])
		return ret

	def evalExpr (self, inside):
		inside = inside.strip()
		exprTokens = re.split(" +", inside)
		if (len(exprTokens) == 1 and Utility().isNumber(exprTokens[0])):
			return exprTokens[0]

		opcode = exprTokens[0]
		# print exprTokens[1:len(exprTokens)]
		# print exprTokens[1:len(exprTokens)]
		thisexpr = ArithmeticExpressionFactory(opcode, exprTokens[1:len(exprTokens)]).getExpr()
		return thisexpr
	def getOpening(self):
		char = self.getChar()
		while char == ' ':
			char = self.getChar()
		if char != '(':
			raise ParseError("Expression must begin with parentheses")


	def openParens(self):
		self.parensStack.push("(")
		self.numOpenParens += 1
	def closeParens(self):
		if self.openParens < 1:
			raise ParseError("Closing parentheses, no opening")
		self.numOpenParens -=1
		self.parensStack.pop()




class Operator(object):
	pass
class Expr (object):
	pass


if __name__ == '__main__':
	interpreter = Interpreter("(+ 5  3)")
	interpreter.interpret()

	interpreter = Interpreter("( (* (+ 5 3) (- 3 5)))")
	interpreter.interpret()

	interpreter = Interpreter("( - 5 3)")
	interpreter.interpret()

	interpreter = Interpreter("(* 40 45)")
	interpreter.interpret()

	interpreter = Interpreter("()")
	interpreter.interpret()




