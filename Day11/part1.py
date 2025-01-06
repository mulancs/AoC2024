
def func(original_nums):
	nums = original_nums
	# print('nums', nums)
	blinks = 0
	while blinks < 75:
		new_nums = []
		for num in nums:
			if num == 0:
				new_nums.append(1)
			elif len(str(num)) % 2 == 0:
				nums_str = str(num)
				mid = len(str(num)) // 2
				num1 = nums_str[0:mid]
				num2 = nums_str[mid:]
				new_nums.extend([int(num1), int(num2)])

			else:
				new_nums.append(2024 * num)
		# print(new_nums)
		nums = new_nums
		blinks += 1

	return len(nums)


def main():
	original_nums = []
	with open('input.txt') as file:
		for line in file:
			original_nums = line.strip().split()
			original_nums = [int(num) for num in original_nums]
			break
	print(func(original_nums))

if __name__ == '__main__':
	main()
