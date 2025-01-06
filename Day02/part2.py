def is_safe_report(lvl):
	if len(lvl) < 2:
		return False 

	dirs = -1

	if 1 <= abs(lvl[0] - lvl[1]) <= 3:
		if lvl[0] < lvl[1]:
			dirs = 0
		elif lvl[0] > lvl[1] :
			dirs = 1
		else:
			return False
	else:
		return False 

	for i in range(1, len(lvl)-1):
		if 1 <= abs(lvl[i] - lvl[i+1]) <= 3:
			if dirs == 0 and lvl[i] < lvl[i+1] :
				continue
			elif dirs == 1 and lvl[i] > lvl[i+1]:
				continue
			else:
				return False
		else:
			return False

	return True

def remove_and_try(lvl):

	for i in range(len(lvl)):
		if is_safe_report(lvl[0:i] + lvl[i+1: len(lvl)]):
			print('new edit', lvl[0:i] + lvl[i+1: len(lvl)])
			return True
	return False

def part2(arr):
	safe = 0
	for lvls in arr:
		if is_safe_report(lvls):
			safe +=1
		else:
			if remove_and_try(lvls):
				print('remove and try', lvls)
				safe +=1 
	return safe

def main():
	arr = []
	with open('input1.txt') as file:
		for line in file:
			levels = line.split()
			arr.append([int(x) for x in levels])
	print(part2(arr))

if __name__ == '__main__':
	main()