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
			self.assertEqual(Utility().isNumber(str(j)), True)

		self.assertEqual(Utility().isNumber("--5", False))
if __name__ == "__main__":
	unittest.main()
	# multiplyer = MultiplicationExpr(5, 3)
	# print multiplyer.calc()

	# subtracter = SubtractionExpr(5, 3)
	# print subtracter.calc()

	# divider = DivisionExpr(5, 3)
	# print divider.calc()

