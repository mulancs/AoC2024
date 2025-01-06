from collections import defaultdict
import copy

rules =defaultdict(list)
lines = []


# def correct_orer(node1, node2):
# 	# print('check', node1, 'to', node2)
# 	queue = []
# 	queue.append(node1)
# 	visited = set()
# 	while queue:
# 		cur = queue.pop()
# 		visited.add(cur)
# 		if node2 == cur:
# 			return True 
# 		for child in rules[cur]:
# 			if child not in visited:
# 				queue.append(child)				
# 	return False


def is_valid(line):
	# print('at line', line)
	# print('start')
	for i in range(len(line)-1):
		for j in range(i+1, len(line)):
			if line[i] in rules[line[j]]:
				return False
	# print('done')
	return True

def func():
	cnt = 0
	for line in lines:
		if is_valid(line):
			# print('line', line)
			cnt += line[len(line)//2]
	return cnt

def main():
	with open('input.txt') as file:
		for line in file:
			if '|' in line:
				nums = line.split('|')
				nums = [int(n) for n in nums]
				rules[nums[0]].append(nums[1])

			if ',' in line:
				nums = line.split(',')
				nums = [int(n) for n in nums]
				lines.append(nums)
	# print('rules', rules)
	# print('lines', lines)
	print(func())

if __name__ == '__main__':
	main()