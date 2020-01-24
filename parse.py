from nodes import *

def generateExpressionTree(expr):
	global expression, pos

	expression = expr
	pos = 0
	exprTree = parseOperation()
	return exprTree

token = None
expression = ""
pos = 0

def parseOperation():
	global token

	left = parseValue()
	right = None

	operation = None

	get()
	if token:
		operation = token
		right = parseOperation()
	else:
		return left

	exprTree = None
	if operation == "+":
		exprTree = AddNode(left, right)
	elif operation == "-":
		exprTree = SubtractNode(left, right)
	elif operation == "*":
		exprTree = MultiplyNode(left, right)
	elif operation == "/":
		exprTree = DivideNode(left, right)
	elif operation == "^":
		exprTree = PowerNode(left, right)

	return exprTree

def parseValue():
	""" passes variable or value """
	global token, expression, pos

	get()

	negative = False
	if token == "-":
		negative = True
		get()

	value = float(token)
	if negative:
		value *= -1

	exprTree = ValueNode(value)
	return exprTree

def get():
	global token, expression, pos

	if pos == len(expression):
		token = None
		return

	token = None

	while expression[pos] == " ":
		pos += 1

	if expression[pos] == "(":
		token = "("
		pos += 1
	elif expression[pos] == "+":
		token = "+"
		pos += 1
	elif expression[pos] == "-":
		token = "-"
		pos += 1
	elif expression[pos] == "*":
		token = "*"
		pos += 1
	elif expression[pos] == "/":
		token = "/"
		pos += 1
	elif expression[pos] == "^":
		token = "^"
		pos += 1
	else:
		if ord(expression[pos]) >= 48 and ord(expression[pos]) <= 57:
			token = ""
			decimalPoint = False
			while True:
				if pos == len(expression):
					break

				character = expression[pos]
				value = ord(character)
				if value >= 48 and value <= 57:
					token += character
				elif value == ".":
					if decimalPoint:
						raise RuntimeError("Invalid number")
					else:
						decimalPoint = True
						token += "."
				else:
					break

				pos += 1
		else:
			raise RuntimeError("Unrecognised character")

def unget():
	pass
