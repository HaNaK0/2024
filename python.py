from vector import Vector
import math

class Line:
	origin: Vector
	k: float
	
	def __init__(self, v1: Vector, v2: Vector):
		self.origin = v1
		vec = v2 - v1
		self.k = vec.y / vec.x
		
	def f(self, x):
		return self.origin.y + self.k * (x - self.origin.x)
		
	def is_on_line(self ,p: Vector):
		return math.isclose(self.f(p.x), p.y)		

def is_inside(vec: Vector, width, height) -> bool:
	return 0 <= vec.x < width and 0 <= vec.y < height

towers: dict[str:list[Vector]] = dict()

height= 0
width= 0

with open('data.txt', 'r') as file:
	for y, line in enumerate(file):
		height = max(height,y + 1)
		width = len(line)
		for x,char in enumerate(line):
			if char != ".":
				towers.setdefault(char, []).append(Vector(x, y))
				
anti_nodes: set[Vector] = set()

for tower_list in towers.values():
	for i, tower_1 in enumerate(tower_list[:-1]):
		for tower_2 in tower_list[i+1:]:
			diff: Vector = (tower_1 - tower_2).nomalized()
			next_t = tower_1
			
			while is_inside(next_t, width, height):
				anti_nodes.add(next_t)
				next_t = next_t + diff
				
			next_t = tower_1 - diff
			while is_inside(next_t, width, height):
				anti_nodes.add(next_t)
				next_t = next_t - diff
			

for x in range(0,width):
	for y in range(0,height):
		if (x,y) in anti_nodes:
			print("#", end="")
		else:
			print(".", end="")
	print()

print(len(anti_nodes))