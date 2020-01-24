class ExpressionNode:
	def output(self, node, isOperation=False):
		if isOperation:
			print("(", end="")
			node.left.output()

			nodeType = type(node)
			
			if (nodeType == AddNode):
				print("+", end="")
			elif (nodeType == SubtractNode):
				print("-", end="")
			elif (nodeType == MultiplyNode):
				print("*", end="")
			elif (nodeType == DivideNode):
				print("/", end="")
			elif (nodeType == PowerNode):
				print("^", end="")
			else:
				raise RuntimeError("Operation type not recognised: ", nodeType)

			node.right.output()
			print(")", end="")
		else:
			nodeType = type(node)

			if nodeType == ValueNode:
				print(node.value, end="")
			elif nodeType == VariableNode:
				print(node.variable, end="")
			else:
				raise RuntimeError("Node not recognised: ", nodeType)

	def evaluate(self, node, isOperation=False):
		if isOperation:
			left = node.left.evaluate()
			right = node.right.evaluate()

			nodeType = type(node)

			if (nodeType == AddNode):
				return left + right
			elif (nodeType == SubtractNode):
				return left - right
			elif (nodeType == MultiplyNode):
				return left * right
			elif (nodeType == DivideNode):
				return left / right
			elif (nodeType == PowerNode):
				return left ** right
			else:
				raise RuntimeError("Operation type not recognised: ", nodeType)
		else:
			nodeType = type(node)

			if nodeType == ValueNode:
				return node.value
			elif nodeType == VariableNode:
				raise RuntimeError("Cannot evaluate variable")
			else:
				raise RuntimeError("Node type not recognised: ", nodeType)

	def simplify(self, node, isOperation=False):
		nodeType = type(node)

		if isOperation:
			left = node.left.simplify()
			right = node.right.simplify()

			if nodeType == AddNode:
				if left.isZero():
					if right.isZero():
						return ValueNode(0)
					else:
						return right
				elif right.isZero():
					return left
				elif left.equals(right):
					return MultiplyNode( ValueNode(2), left )
				else:
					return AddNode(left, right)
			elif nodeType == SubtractNode:
				if left.isZero():
					if right.isZero():
						return ValueNode(0)
					else:
						return right.negate()
				elif right.isZero():
					return left
				elif left.equals(right):
					return ValueNode(0)
				else:
					return SubtractNode(left, right)
			elif nodeType == MultiplyNode:
				if left.isZero() or right.isZero():
					return ValueNode(0)
				elif left.isOne():
					return right
				elif right.isOne():
					return left
				elif left.equals(right):
					return PowerNode( ValueNode(2), left )
				else:
					return MultiplyNode(left, right)
			elif nodeType == DivideNode:
				if left.isZero():
					return ValueNode(0)
				elif right.isOne():
					return left
				elif left.equals(right):
					return ValueNode(1)
				else:
					return DivideNode(left, right)
			elif nodeType == PowerNode:
				if left.isZero():
					return ValueNode(0)
				elif right.isZero():
					return ValueNode(1)
				else:
					return PowerNode(left, right)
			else:
				raise RuntimeError("Node type not recognised: ", nodeType)
		else:

			if nodeType == ValueNode:
				return ValueNode(node.value)
			elif nodeType == VariableNode:
				return VariableNode(node.variable)
			else:
				raise RuntimeError("Node tye not recognised: ", nodeType)

	def equals(self, node, expr, isOperation=False):
		nodeType = type(node)
		exprType = type(expr)

		if nodeType != exprType:
			return False

		if isOperation:
			if nodeType == AddNode:
				if node.left.equals(expr.left):
					if not node.right.equals(expr.right):
						return False
				elif node.left.equals(expr.right):
					if not node.right.equals(expr.left):
						return False
				else:
					return False
			elif nodeType == SubtractNode:
				if not node.left.equals(expr.left):
					return False
				elif not node.right.equals(expr.right):
					return False
			elif nodeType == MultiplyNode:
				if node.left.equals(expr.left):
					if not node.right.equals(expr.right):
						return False
				elif node.left.equals(expr.right):
					if not node.right.equals(expr.left):
						return False
				else:
					return False
			elif nodeType == DivideNode:
				if not node.left.equals(expr.left):
					return False
				elif not node.right.equals(expr.right):
					return False
			elif nodeType == PowerNode:
				if not node.left.equals(expr.left):
					return False
				elif not node.right.equals(expr.right):
					return False
			else:
				raise RuntimeError("Node type not recognised: ", nodeType)
		else:
			if nodeType == ValueNode:
				if node.value != expr.value:
					return False
			elif nodeType == VariableNode:
				if node.variable != expr.variable:
					return False
			else:
				raise RuntimeError("Node type not recognised: ", nodeType)

		return True

	def isZero(self, node):
		nodeType = type(node)
		if nodeType == ValueNode:
			return node.value == 0
		return False

	def isOne(self, node):
		nodeType = type(node)
		if nodeType == ValueNode:
			return node.value == 1
		return False

class Operation(ExpressionNode):
	def __init__(self, left=None, right=None):
		self.left = left
		self.right = right

	def output(self, node):
		super().output(node, True)

	def evaluate(self, node):
		return super().evaluate(node, True)

	def simplify(self, node):
		return super().simplify(node, True)

	def equals(self, node, expr):
		return super().equals(node, expr, True)

class ValueNode(ExpressionNode):
	def __init__(self, value=0):
		self.value = value

	def output(self):
		super().output(self)

	def evaluate(self):
		return super().evaluate(self)

	def simplify(self):
		return super().simplify(self)

	def equals(self, expr):
		return super().equals(self, expr)

	def isZero(self):
		return super().isZero(self)

	def isOne(self):
		return super().isOne(self)

class VariableNode(ExpressionNode):
	def __init__(self, variable=""):
		self.variable = variable

	def output(self):
		super().output(self)

	def evaluate(self):
		return super().evaluate(self)

	def simplify(self):
		return super().simplify(self)

	def equals(self, expr):
		return super().equals(self, expr)

	def isZero(self):
		return super().isZero(self)

	def isOne(self):
		return super().isOne(self)

class AddNode(Operation):
	def __init__(self, left=None, right=None):
		super().__init__(left, right)

	def output(self):
		super().output(self)

	def evaluate(self):
		return super().evaluate(self)

	def simplify(self):
		return super().simplify(self)

	def equals(self, expr):
		return super().equals(self, expr)

class SubtractNode(Operation):
	def __init__(self, left=None, right=None):
		super().__init__(left, right)

	def output(self):
		super().output(self)

	def evaluate(self):
		return super().evaluate(self)

	def simplify(self):
		return super().simplify(self)

	def equals(self, expr):
		return super().equals(self, expr)

class MultiplyNode(Operation):
	def __init__(self, left=None, right=None):
		super().__init__(left, right)

	def output(self):
		super().output(self)

	def evaluate(self):
		return super().evaluate(self)

	def simplify(self):
		return super().simplify(self)

	def equals(self, expr):
		return super().equals(self, expr)

class DivideNode(Operation):
	def __init__(self, left=None, right=None):
		super().__init__(left, right)

	def output(self):
		super().output(self)

	def evaluate(self):
		return super().evaluate(self)

	def simplify(self):
		return super().simplify(self)

	def equals(self, expr):
		return super().equals(self, expr)

class PowerNode(Operation):
	def __init__(self, left=None, right=None):
		super().__init__(left, right)

	def output(self):
		super().output(self)

	def evaluate(self):
		return super().evaluate(self)

	def simplify(self):
		return super().simplify(self)

	
