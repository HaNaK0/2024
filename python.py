from dataclasses import dataclass
from vector import Vector
from typing import Self
from collections import deque
import itertools

directions = [(-1,0), (0,-1), (1,0),(0,1)]

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
		y = self.height
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

@dataclass
class State:
	level: int
	head: int
	pos: Vector
	back: Self = None
	
	def check(self, map: GridMap):
		out = []
		for dir in directions:
			point = self.pos + dir
			if map.is_inside(point):
				val = map.get(point)
				diff = val - self.level
				if diff == 1:
					out.append(State(val, self.head, point, back=self.back))
		return out

	def get_trail(self) -> list[Self]:
		if self.back is not None:
			return self.back.get_trail() + [self]
		else:
			return [self]

trail_map = GridMap(0,0)

with open("data.txt", "r") as file:
	for line in file:
		trail_map.add_row(line.strip())
		
trail_heads = [State(0,i, v) for i, v in enumerate(trail_map.find_all(0))]


state_queu = deque()
ends = [set() for s in trail_heads]
trails: list[State] = []

state_queu.extend(trail_heads)

while len(state_queu) > 0:
	state: State = state_queu.popleft()
	if state.level >= 9:
		ends[state.head].add(state.pos)
		trails.append(state)
	else:
		states = state.check(trail_map)
		state_queu.extend(states)

scores = [len(s) for s in ends]
total = 0
for score in scores:
	total+= score
	
print(total)
