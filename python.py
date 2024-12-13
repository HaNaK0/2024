from dataclasses import dataclass

@dataclass
class File:
	location: int
	size: int

line: str = ""

with open('data.txt', 'r') as file:
	line = file.readline()

disk: list[int] = []
files: list[File] = []
spaces: list[File] = []

for i, c in enumerate(line):
	entry = int(c)
	if i % 2 == 0 and entry != 0:
		files.append(File(len(disk), entry))
	elif entry != 0:
		spaces.append(File(len(disk), entry))
	
	for j in range(0, entry):
		disk.append(int(i / 2) if i % 2 == 0 else -1)
		
for file in reversed(files):
	for space in spaces:
		if space.location >= file.location:
			break
		
		if space.size >= file.size:
			disk[space.location:space.location+ file.size] = disk[file.location:file.location+file.size]
			for i in range(file.location, file.location+file.size):
				pass
				disk[i]= -1
			if space.size == file.size:
				spaces.remove(space)
			else:
				space.size = space.size - file.size
				space.location += file.size
			break
		
		
result = 0

for  index, block in enumerate(disk):
	if block < 0:
		continue
	
	result += index * block

print(result)
with open("out.txt", "w") as file:
	file.write(str(result))
