from collections import defaultdict
import copy

rules =defaultdict(list)
lines = []
inorder = defaultdict(list)

def correct_line(line):
	print('correcting the line', line)
	in_orders = {}
	for node in line:
		in_orders[node] = 0

	for node in in_orders.keys():
		in_orders[node] = list(set(line) & set(inorder[node]))

	print('in_orders', in_orders)
	new_line = []
	while len(in_orders) > 0:
		# print('new_line', new_line)
		nodes_with_zero_in = []
		for key in in_orders.keys():
			if len(in_orders[key]) == 0:
				nodes_with_zero_in.append(key)
				new_line.append(key)
				del in_orders[key]

		for node in nodes_with_zero_in:
			for key in in_orders.keys():
				if node in in_orders[key]:
					in_orders[key].remove(node)
	print('new_line', new_line)
	return new_line #new_line

def is_valid(line):
	for i in range(len(line)-1):
		for j in range(i+1, len(line)):
			if line[i] in rules[line[j]]:
				return False
	return True

def func():
	cnt = 0
	for line in lines:
		if not is_valid(line):
			new_line = correct_line(line)
			cnt += new_line[len(new_line)//2]

	return cnt

def main():
	with open('input.txt') as file:
		for line in file:
			if '|' in line:
				nums = line.split('|')
				nums = [int(n) for n in nums]
				rules[nums[0]].append(nums[1])
				inorder[nums[1]].append(nums[0])

			if ',' in line:
				nums = line.split(',')
				nums = [int(n) for n in nums]
				lines.append(nums)

	print(func())

if __name__ == '__main__':
	main()