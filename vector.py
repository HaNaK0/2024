import unittest
from fractions import Fraction
from typing import Self

class Vector:
	x: int
	y: int
	
	def __init__(self, x ,y):
		self.x = x
		self.y = y
		
	@classmethod
	def from_tuple(cls, t: tuple[int,int]) -> Self:
		return Vector(t[0], t[1])
	
	def as_tuple(self) -> tuple[int, int]:
		return (self.x, self.y)
	
	def __add__ (self, other) -> Self:
		match other:
			case v if isinstance(v, Vector):
				return Vector(self.x + v.x, self.y + v.y)
			case (int(x), int(y)):
				return Vector(self.x + x, self.y + y)
			case _:
				raise TypeError(f"cant add a {type(other)} to a vector")
				
	def __sub__ (self, other) -> Self:
		match other:
			case v if isinstance(v, Vector):
				return Vector(self.x - v.x, self.y - v.y)
			case (int(x), int(y)):
				return Vector(self.x - x, self.y - y)
			case _:
				raise TypeError(f"cant add a {type(other)} to a vector")
	
	
	def __eq__(self, other) -> bool:
		match other:
			case v if isinstance(v, Vector):
				return v.x == self.x and v.y == self.y
			case (int(x), int(y)):
				return self.x == x and self.y == y
			case _:
				raise TypeError(f"can't compare a vector with an object of type {type(other)}")
	
	def __mul__(self, other) -> Self:
		if not isinstance(other, int):
			raise TypeError(f"Can't multiply a Vector with a {type(other)}")
		
		return Vector(self.x * other, self.y * other)
		
	def __str__(self) -> str:
			return f"Vector({self.x}, {self.y})"
			
	def __hash__(self):
			return hash((self.x, self.y))
			
	def __neg__(self) -> Self:
			return self *-1
		
	def nomalized(self) -> Self:
			if self.y == 0:
				return Vector(0 if self.x == 0 else 1, 0)
			
			frac= Fraction(self.x, self.y)
			result = Vector(frac.numerator, frac.denominator)
			return result if self.y > 0 else - result
			
	def is_within(self, size: tuple[int, int], origin = (0,0)):
	 	origin = Vector.from_tuple(origin)
	 	max = origin + size
	 	return origin.x <= self.x < max.x and origin.y <= self.y < max.y
	 	
			
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
				def test_from_tuple(self):
					v = Vector.from_tuple((0,5))
					
					self.assertEqual(v, (0,5))
					
				def test_normalize(self):
					v = Vector(10,30)
					self.assertEqual(v.nomalized(), (1,3))
					
					v2 = Vector(5,0)
					self.assertEqual(v2.nomalized(), (1,0))
					
					v3 = Vector(0,5)
					self.assertEqual(v3.nomalized(), (0,1))
					
					v4 = Vector(6,-4)
					self.assertEqual(v4.nomalized(), (3,-2))

if __name__ == "__main__":
	unittest.main()
	