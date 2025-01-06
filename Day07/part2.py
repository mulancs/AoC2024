
def recursion(target, running_sum, nums):
	print('target', target, 'nums', nums)
	if len(nums) == 0 :
		if target == running_sum:
			return True
		else:
			return False 

	return recursion(target, running_sum + nums[0], nums[1:]) or recursion(target, running_sum * nums[0], nums[1:])

ans = 0

with open('input.txt') as file:
	for line in file:
		line = line.split()
		arr = [int(line[0].strip(':'))] + [int(x) for x in line[1:]]
		print('checking', arr)
		if recursion(arr[0], arr[1], arr[2:]):
			# print('target', arr[0])
			ans += arr[0]
print(ans)