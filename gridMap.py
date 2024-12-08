from vector import Vector

class GridMap:
	width: int
	height: int
	store: list[int]
	
	def __init__(self, width:int, height:int):
		self.width = width
		self.height = height
		
		self.store = [-1] * (width * height)
		
	def add(self, pos: Vector, data:int):
		self.store[self._vec_to_i(pos)] = data
		
	def add_row(self, row):
		self.height +=1
		self.width = len(row)
		
		for c in row:
			self.store.append(int(c))
			
	def get(self, pos:Vector):
		return self.store[self._vec_to_i(pos)]
		
	def is_inside(self, vec: Vector) -> bool:
		return 0 <= vec.x < self.width and 0 <= vec.y < self.height
	
	def find_all(self, goal) -> list[Vector] :
		out = []
		for i, entry in enumerate(self.store):
			if entry == goal:
				p = Vector(i % self.width, int(i / self.width))
				out.append(p)
		return out
		
	
	def _vec_to_i(self, pos: Vector) -> int :
		return self.width * pos.y + pos.x
		
	def __str__(self):
		out = ""
		for y in range(0, self.height):
			for x in range(0, self.width):
				point = Vector(x,y)
				val = self.store[self._vec_to_i(point)]
				out += str(val) if val >= 0 else "."
			out += "\n"
		return out