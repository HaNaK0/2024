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

stones: dict[int:int] = {}

with open("data.txt", "r") as file:
        line = file.readline().strip()
        stones = {int(c):1 for c in line.split(" ")}

for i in range(0,75):
	new_stones = dict()
	for stone, amount in stones.items():
		for s in blink_one(stone):
			if s in new_stones:
				new_stones[s] += amount
			else:
				new_stones[s] = amount
				
	stones = new_stones
					
print(sum(stones.values()))
with open("out.txt", "w") as file:
	file.write(str(sum(stones.values())))
