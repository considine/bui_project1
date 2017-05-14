from SchemeInterpreter import *
import unittest

class TestArithmeticExpressions(unittest.TestCase):
	def testAdd (self):
		for i in xrange(100):
			for j in xrange(100):
				adder = AdditionExpr (i, j)
				self.assertEqual(adder.calc(), i + j)
	def testSubtract (self):
		for i in xrange(100):
			for j in xrange(100):
				subtracter = SubtractionExpr (i, j)
				self.assertEqual(subtracter.calc(), i - j)

	def testMultiply (self):
		for i in xrange(100):
			for j in xrange(100):
				multiplyer = MultiplicationExpr (i, j)
				self.assertEqual(multiplyer.calc(), i * j)



class TestUtilities(unittest.TestCase):
	def testIsNumber(self):
		for i in xrange(1000):
			j =  (i - 500) / 10
			self.assertEqual(Utility.isNumber(str(j)), True)

		self.assertEqual(Utility.isNumber("--5"), False)

class TestListTypes (unittest.TestCase):
	def testIsEmpty(self):
		lf = ListFactory(" ")
		l = lf.getList()
		self.assertEqual (l.checkType() == Utility.emptyType(), True)
	def testIsNotEmpty(self):
		lf = ListFactory("d")
		l = lf.getList()
		self.assertEqual (l.checkType() == Utility.nonEmptyType(), True)

		lf = ListFactory("()")
		l = lf.getList()
		self.assertEqual (l.checkType() == Utility.nonEmptyType(), True)
class TestArithmeticInput (unittest.TestCase):
	def testProperMath(self):
		interpreter = Interpreter("(* 40 45)")
		self.assertEqual(interpreter.interpret(), 1800)

		interpreter = Interpreter("( (* (+ 5 3) (- 3 5)))")
		self.assertEqual(interpreter.interpret(), -16)



if __name__ == "__main__":
	unittest.main()

