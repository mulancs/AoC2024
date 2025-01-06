def is_safe_report(lvl):
	if len(lvl) < 2:
		return False 

	dirs = -1
	if lvl[0] < lvl[1] and 1 <= abs(lvl[0] - lvl[1]) <= 3:
		dirs = 0
	elif lvl[0] > lvl[1] and 1 <= abs(lvl[0] - lvl[1]) <= 3:
		dirs = 1
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

def part1(arr):
	safe = 0
	for lvls in arr:
		if is_safe_report(lvls):
			safe +=1
			print('lvls', lvls)
	return safe

def main():
	arr = []
	with open('input1.txt') as file:
		for line in file:
			levels = line.split()
			arr.append([int(x) for x in levels])
	print(part1(arr))

if __name__ == '__main__':
	main()