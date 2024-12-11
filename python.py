from vector import Vector

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
			diff = tower_1 - tower_2
			if is_inside(tower_1 + diff, width, height):
				anti_nodes.add(tower_1 + diff)
			if is_inside(tower_2 + -diff, width, height):
				anti_nodes.add(tower_2 + -diff)

print(len(anti_nodes))