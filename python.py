
class Guard:
	x: int
	y: int
	dir: int
	steps: set[tuple]
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
		
		self.steps = set([self.get_pos()])
				
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
		(self.x, self.y) = self.get_next()
		self.steps.add(self.get_pos())
		
	def is_on_map(self, map_width, map_height) -> bool:
		return 0 <= self.x < map_width and 0 <= self.y < map_height
		
	def get_pos(self) -> tuple[int,int]:
		return (self.x,self.y)
	
	def get_steps(self) -> int:
		return len(self.steps)
		

obstacles: set[tuple[int,int]] = set()
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

print(guard.get_steps()-1)
