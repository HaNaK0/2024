	
def test(target, values) -> bool:
	if values[0] > target:
		return False
	if len(values) == 1:
		return target == values[0]
	if (test(target, [values[0] + values[1]] + values[2:])):
		return True
	if (test(target, [values[0] * values[1]] + values[2:])):
		return True
	val_str = str(values[0]) + str(values[1])
	if test(target, [int(val_str)] + values[2:]):
		return True
	return False

final_result = 0

with open('data.txt', 'r') as file:
			for line in file:
				(cal, vals) = line.strip().split(":")
				cal = int(cal)
				
				vals = [int(val) for val in vals.strip().split(" ")]
				if test(cal, vals):
						final_result += cal
						
print(final_result)

with open("out.txt","w") as file:
	file.write(str(final_result))
