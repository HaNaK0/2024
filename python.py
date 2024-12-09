
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
			
for update in updates:
	is_ok = True
	for (page_1, page_2) in rules:
		if page_1 not in update or page_2 not in update:
			continue
		
		if update.index(page_1) > update.index(page_2):
			is_ok = False
			break
	
	if is_ok:
		middle_num = update[int(len(update)/2)]
		result += middle_num

print(result)
			