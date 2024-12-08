import concurrent.futures

def blink_one(stone: int) -> list[int]:
	if stone == 0:
		return [1]
		
	s_str = str(stone)
	if len(s_str) % 2 == 0:
		half = int(len(s_str)/ 2)
		return [int(s_str[:half]), int(s_str[half:])]
	
	return [stone * 2024]
 	
def blink(stones: list[int])-> list[int]:
	out = list()
	for stone in stones:
		stone_str = str(stone)
		if stone == 0:
			out.append(1)
		elif len(stone_str) % 2 == 0:
			half = int(len(stone_str) / 2)
			out.append(int(stone_str[:half]))
			out.append(int(stone_str[half:]))
		else:
			out.append(stone * 2024)
			
	return out
			

stones: list[int] 

with open("data.txt", "r") as file:
	line = file.readline().strip()
	stones = [int(c) for c in line.split(" ")]


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
	for i in range(0,75):
		result = list()
		for out in executor.map(blink_one, stones):
			result.extend(out)
		stones = result
		print(i)
	print(len(stones))
