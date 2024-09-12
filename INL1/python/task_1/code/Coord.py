class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		if isinstance(other, Coord):
			return self.x == other.x and self.y == other.y
		return False

	def __repr__(self):
		return f"({self.x}, {self.y})"

	def move(self, x_delta, y_delta):
		self.x += x_delta
		self.y += y_delta
