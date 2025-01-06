from collections import Counter

def part2(arr1, arr2):
	counter2 = Counter(arr2)

	dis = 0
	for i in range(len(arr1)):
		dis += arr1[i] * counter2[arr1[i]]
	return dis

def main():
	arr1, arr2 = [], []
	with open('input1.txt') as file:
		for line in file:
			nums = line.split()
			arr1.append(int(nums[0]))
			arr2.append(int(nums[1]))
	print(part2(arr1, arr2))

if __name__ == '__main__':
	main()