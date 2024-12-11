import unittest

class Vector:
	x: int
	y: int
	
	def __init__(self, x ,y):
		self.x = x
		self.y = y
	
	def as_tuple(self) -> tuple[int, int]:
		return (self.x, self.y)
	
	def __add__ (self, other):
		match other:
			case v if isinstance(v, Vector):
				return Vector(self.x + v.x, self.y + v.y)
			case (int(x), int(y)):
				return Vector(self.x + x, self.y + y)
			case _:
				raise TypeError(f"cant add a {type(other)} to a vector")
				
	def __sub__ (self, other):
		match other:
			case v if isinstance(v, Vector):
				return Vector(self.x - v.x, self.y - v.y)
			case (int(x), int(y)):
				return Vector(self.x - x, self.y - y)
			case _:
				raise TypeError(f"cant add a {type(other)} to a vector")
	
	
	def __eq__(self, other):
		match other:
			case v if isinstance(v, Vector):
				return v.x == self.x and v.y == self.y
			case (int(x), int(y)):
				return self.x == x and self.y == y
			case _:
				raise TypeError(f"can't compare a vector with an object of type {type(other)}")
	
	def __mul__(self, other):
		if not isinstance(other, int):
			raise TypeError(f"Can't multiply a Vector with a {type(other)}")
		
		return Vector(self.x * other, self.y * other)
		
	def __str__(self):
			return f"Vector({self.x}, {self.y})"
			
	def __hash__(self):
			return hash((self.x, self.y))
			
	def __neg__(self):
			return self *-1
			
			
class VectorTest(unittest.TestCase):
				def test_eq(self):
					self.assertTrue(Vector(1,1) == Vector(1,1))
					self.assertFalse(Vector(1,1) == Vector(0,1))
					self.assertTrue(Vector(1,1) == (1,1))
					self.assertFalse(Vector(1,1) == (1,0))
					with self.assertRaises(TypeError):
						_ = Vector(1,1) == 1
				
				def test_add(self):
						v1 = Vector(1,1)
						v2 = Vector(1,1)
						
						self.assertEqual(v1 + v2, (2,2))
						self.assertEqual(v1 + (3,4), (4,5))
						with self.assertRaises(TypeError):
							_ = v1 + 1
					
				def test_sub(self):
						v1 = Vector(5,3)
						v2 = Vector(2,3)
						
						self.assertEqual(v1-v2, (3,0))
						self.assertEqual(v1-(1,1), (4,2))
						with self.assertRaises(TypeError):
							_ = v1 - 1
				
				def test_hash(self):
					v1 = Vector(1,1)
					v2 = Vector(1,4)
					
					self.assertNotEqual(hash(v1), hash(v2))
				
				def test_neg(self):
					v = Vector(1,-1)
					
					self.assertEqual(-v, (-1, 1))
					
				def test_mul(self):
						v = Vector(2,2)
						
						self.assertEqual(v * 2, (4, 4))
						with self.assertRaises(TypeError):
							_ = v * (0,0)
													
if __name__ == "__main__":
	unittest.main()
	
