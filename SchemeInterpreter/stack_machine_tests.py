from stack_machine import ParserStack
from stack_machine import PopError

from stack_machine import Interpreter










def testInterpreter ():
	interpreter = Interpreter()
	interpreter.interpret("(+ (+ 4 1)(+)(()()))")




def testStack ():
	stack =  ParserStack()
	stack.push(5)
	print stack.getTop()
	stack.push(6)
	print stack.getTop()

	print "Popping first item"
	stack.pop()
	print "Popping second item"
	stack.pop()
	print "Popping third item"
	try:
		stack.pop()
	except:
		print "properly thrown exception"


	strStack = ParserStack()
	i=0
	while i < 1000:
		strStack.push(str(i))
		i+=1


	while True:
		

		try:
			# print strStack.getTop()
			strStack.pop()
		except PopError:
			break

	print "Popped all!";












if __name__ == "__main__":
	testInterpreter()
