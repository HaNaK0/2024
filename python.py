
class Guard:
	x: int
	y: int
	dir: int
	steps: dict[tuple[int,int], int]
	def __init__(self, x, y, dir:str):
		self.x = x
		self.y = y
		match dir:
			case "^":
				self.dir = 0
			case ">":
				self.dir = 1
			case "v":
				self.dir = 2
			case "<":
				self.dir = 3
			case _:
				raise Exception(f"invalid symbol for direction:{dir}")
		
		self.steps = dict()
				
	def get_next(self) -> tuple[int, int]:
		match self.dir:
			case 0:
				return (self.x, self.y-1)
			case 1:
				return (self.x+1, self.y)
			case 2:
				return (self.x, self.y+1)
			case 3:
				return (self.x-1,self.y)
			case _:
				raise Exception(f"invalid direction {self.dir}")
		
	def turn(self):
		self.dir = (self.dir + 1) % 4
		
	def step(self):
		self.steps.setdefault(self.get_pos(), []).append(self.dir)
		(self.x, self.y) = self.get_next()
		
	def is_on_map(self, map_width, map_height) -> bool:
		return 0 <= self.x < map_width and 0 <= self.y < map_height
		
	def get_pos(self) -> tuple[int,int]:
		return (self.x,self.y)
	
	def get_steps(self) -> int:
		return len(self.steps)
		
	def get_if_looping(self)->bool:
		return self.get_pos() in self.steps and self.dir in self.steps[self.get_pos()]
		

obstacles: set[tuple[int,int]] = set()
origin: tuple[int,int,str]
guard: Guard

width: int
height: int

with open('data.txt', 'r') as file:
			y = 0
			lines = file.readlines()
			height = len(lines)
			width = len(lines[0].strip())
			for line in lines:
				x= 0
				for char in line.strip():
					match char:
						case "#":
							obstacles.add((x,y))
						case ">" | "v" | "<" | "^":
							guard = Guard(x,y,char)
							origin = (x,y,char)
						case ".":
							pass
						case _:
							raise Exception("invalid charachter in input: {char}")
					x += 1
				y+=1

while guard.is_on_map(width, height):
			if guard.get_next() in obstacles:
				guard.turn()
			else:
				guard.step()

print(guard.get_steps())

original_path = guard.steps
result = 0

del original_path[(origin[0], origin[1])]

for pos in original_path:
	obstacles.add(pos)
	guard = Guard(origin[0], origin[1], origin[2])
	
	while guard.is_on_map(width, height):
		if guard.get_next() in obstacles:
			guard.turn()
		else:
			guard.step()
		
		if guard.get_if_looping():
			result +=1
			break
	
	obstacles.remove(pos)

print(result)
