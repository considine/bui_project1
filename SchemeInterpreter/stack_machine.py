from abc import ABCMeta, abstractmethod
import re

class ListExpr:
	pass

class Utility(object):
	def __init__(self):
		pass
	@staticmethod
	def isNumber(s):
		try:
			float(s)
			return True
		except ValueError:
			return False

	# CONSTANTS
	@staticmethod
	def emptyType():
		return 0
	@staticmethod
	def nonEmptyType():
		return 1 # arbitrary codes



class LispList(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		pass
	@abstractmethod
	def car(self):
		pass

	@abstractmethod
	def ctr(self):
		pass

	@property
 	def listType (self):
 		raise NotImplementedError
 	@abstractmethod
	def checkType(self):
		pass




class LispEmptyList(LispList):
	def __init__(self):
		pass
	def car(self):
		raise EmptyListCar("Cannot reference Car of empty List")
	def ctr (self):
		raise EmptyListCtr("Cannot reference Ctr of empty List")
	def checkType (self):
		return Utility.emptyType()
	def __str__(self):
		return "List()"

class LispNonemptyList(LispList):
	def __init__(self, listString):
		self.listString = listString.replace(",", " ")
		# remove multiple spaces in a row
		self.listString = re.sub(r' +', " ", self.listString)
	def __str__(self):
		return "List(" + self.listString + ")"
	def checkType (self):
		return Utility.nonEmptyType()
	def car (self):
		return self.listString.strip().split(" ")[0]
	def ctr(self):
		its = self.listString.strip().split(" ")
		itsLen = len(its)
		lf = ListFactory(" ".join(its[1: itsLen]))
		return lf.getList()




class ListFactory (object):
	""" Takes the string inside of List parens, and returns an object
	of class LispList. This means a LispEmptyList if there is nothing but
	space between the parens, and a LispNonemptyList if there is """
	def __init__(self, innerparensString):
		setlist = False
		for char in innerparensString:
			if (char != ' '):
				self.list = LispNonemptyList(innerparensString)
				setlist = True
		# print setlist
		if not setlist: self.list = LispEmptyList()
	def getList(self):
		return self.list


class GeneralExpr:
	def __init__(self):
		raise Exception("Instantiating a baseclass")
	def calc(self):
		return self.result


class CarListExpr(GeneralExpr):
	def __init__(self, list):
		self.result = list.car()

class CtrListExp(GeneralExpr):
	def __init__(self, list):
		self.result = list.ctr()



class ArithmeticExpr(GeneralExpr):
	def __init__(self):
		super(GeneralExpr, self).__init__();
	


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
	""" Returns an Expression based on the operation code. Will return an arithmetic expression 
	if the op code is +-/*, a List Expression if the operation is ctr or car, and a conditionalExpression
	if the opcode is cond  """
	

	def __init__(self, opcode, kargs):
		
		arithmeticOps = ["+", "-", "*", "/"]
		listOps = ["ctr", "car"]
		conditionalListOps = ["cond", "eq?", "else"]
		if (opcode in arithmeticOps):
			self.expr = self.getArithmeticOp(opcode, kargs)
		elif (opcode in listOps):
			self.expr = self.getListOperation(opcode, kargs[0])
	# def getListOperation(self, opcode, kargs):


	def  getArithmeticOp(self, opcode, kargs):
		opcodemap = {
			"+" : AdditionExpr(float(kargs[0]), float(kargs[1])).result,
			"-" : SubtractionExpr(float(kargs[0]), float(kargs[1])).result,
			"*" : MultiplicationExpr(float(kargs[0]), float(kargs[1])).result,
			"/" : DivisionExpr(float(kargs[0]), float(kargs[1])).result

		}	
		return opcodemap[opcode]
	def getListOperation (self, opcode, lstring):
		opcodemap = {
			"car" : CarListExpr(ListFactory(lstring).getList()).result,
			"ctr" : CtrListExp(ListFactory(lstring).getList()).result

		}
		return opcodemap[opcode]
	def getExpr(self):
		return self.expr



	

class ParserStack(object):
	def __init__(self):
		self.l = []
	def push(self, item):
		self.l = [item] + self.l
		

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

class EmptyListError(IndexError):
	def __init__(self, message):
		super(IndexError, self).__init__(message)

class EmptyListCtr(EmptyListError):
	def __init__(self, message):
		super(EmptyListError, self).__init__(message)
class EmptyListCar(EmptyListError):
	def __init__(self, message):
		super(EmptyListError, self).__init__(message)


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
	def getListToken (self):
		""" followed by a list operation, searched for 'List' followed by
		stack beginning and ending with parens. This function finds the string,
		returns what's between the parentheses and adjusts the index properly """
		if self.index + 4 < len(self.text):
			if self.text[self.index : self.index+4] == "List":
				self.index+=4
				return True
		return False

	def getListString(self):
		""" after a list is confirmed, get the parens, and everything between"""
		self.getOpening()
		# self.openParens()
		listinner = ''
		done = self.numOpenParens
		while self.numOpenParens != done -1:
			
			nchar = self.getChar()
			
			
			if (nchar == ")"):
				
				self.closeParens()
			elif (nchar == "("):
				self.openParens()
			listinner += nchar
	
		return listinner[0:len(listinner)-1]
	def interpret(self):
		self.getOpening()
		
		expr = self.getExpr(self.numOpenParens -1) 
		return expr

	# def getList(self):
		



	def getExpr(self, stackCount):
		inner = ''
		
		while self.numOpenParens != stackCount:
			nchar = self.getChar()
			if self.getListToken():
				# print inner + " List(" +self.getListString() + ")"	
				lstring = self.getListString()
				lstring = re.sub(r' +', ",", lstring)
				
				return self.evalExpr(inner + " " +  lstring)


			elif (nchar == ")"):
				self.closeParens()
			elif (nchar == "("):
				self.openParens()
				nchar = str(self.getExpr(self.numOpenParens - 1)) + " "

				
				
			inner += str(nchar)
		# return inner[0:len(inner)-1]
		if (len(inner) == 1):
			return ""
		
		return  self.evalExpr(inner[0:len(inner)-1])
		

	def evalExpr (self, inside):
		inside = inside.strip()
		exprTokens = re.split(" +", inside)
		if (len(exprTokens) == 1 and Utility.isNumber(exprTokens[0])):
			return float(exprTokens[0])
		
		opcode = exprTokens[0]
		
		thisexpr = ExpressionFactory(opcode, exprTokens[1:len(exprTokens)]).getExpr()
		return thisexpr
	def getOpening(self):
		char = self.getChar()
		while char == ' ':
			char = self.getChar()
			# self.index+=1
		if char != '(':
			raise ParseError("Expression must begin with parentheses")
		self.openParens()
		# self.index+=1


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
	
	interpreter = Interpreter("(ctr List (3 5 2 3 2)))")
	print interpreter.interpret()


	
	# it = LispNonemptyList("3 4 5")

	# print it.ctr().ctr().car()

