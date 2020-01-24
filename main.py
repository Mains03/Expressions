from nodes import *
from parse import generateExpressionTree

expression = "2*(2+2)"
expression = generateExpressionTree(expression)
expression.output()
print()
