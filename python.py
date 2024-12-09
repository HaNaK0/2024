
rules: list[tuple[int,int]] = []
updates: list[list[int]] = []

with open('data.txt', 'r') as file:
		parsing_rules = True
		
		for line in file:
			if line == "\n":
				parsing_rules = False
				continue
			
			if parsing_rules:
				split = line.split('|')
				rules.append((int(split[0]),int(split[1])))
			else:
				split = line.split(',')
				update = []
				for entry in split:
					update.append(int(entry))
				updates.append(update)

result = 0
to_be_sorted: list[list[int]] = []
print(to_be_sorted)
		
for update in updates:
	for (page_1, page_2) in rules:
		if page_1 not in update or page_2 not in update:
			continue
		
		if update.index(page_1) > update.index(page_2):
			to_be_sorted.append(update)
			break
			
			
for update in to_be_sorted:
	swapped = True
	while swapped:
		swapped = False
		for (page_1,page_2) in rules:
			if page_1 not in update or page_2 not in update:
				continue
			
			if update.index(page_1) > update.index(page_2):
				update.remove(page_1)
				update.insert(update.index(page_2),page_1)
				swapped = True

for update in to_be_sorted:
	result += update[int(len(update)/2)]

print(result)