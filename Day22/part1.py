
ITERS = 10

def next_secret(num):
	arr = [num]

	for _ in range(ITERS):
		num = (num * 64) ^ num 
		num = num % 16777216

		num = (num // 32) ^ num 
		num = num % 16777216
		
		num = (num * 2048) ^ num 
		num = num % 16777216
		
		arr.append(num)

	return arr

def price_changes(nums):
	price_changes = []
	for i in range(1, len(nums)):
		price_changes.append( (nums[i] - nums[i-1]) % 10)
	return price_changes

def four_prices_generator(arr):
	seqs = []
	for i in range(len(arr)-3):  #n-4 n-3 n-2 n-1
		seqs.append(tuple(arr[i:i+4]))
	return seqs

def track_first_occurence(seqs, arr):
	first_occurence = {}

	for i, sequence in enumerate(seqs):
		if sequence not in first_occurence:
			first_occurence[sequence] = arr[i+3]
	return first_occurence

def find_best_sequence(arrs):
	best_sequence = None
	max_bananas = 0

	sequence_bananas = {}

	for price_changes, prices in arrs:
		sequences = four_prices_generator(price_changes)
		first_occurences = track_first_occurence(sequences, prices)
		for sequence, price in first_occurences.items():
			if sequence not in sequence_bananas:
				sequence_bananas[sequence] = 0 
			sequence_bananas[sequence] += price

	for sequence, total_bananas in sequence_bananas.items():
		if total_bananas > max_bananas:
			best_sequence = sequence
			max_bananas = total_bananas

	return best_sequence, max_bananas

def main():
	nums = []
	with open('input.txt') as file:
		for line in file:
			line = line.strip().split()
			nums.append(int(line[0]))

	nums = [123]
	changes = []
	ones = []
	itr = 0 
	sequence = []
	all_buyers_price_changes = []
	for num in nums:
		secret_nums_arr = next_secret(num)
		changes_arr = price_changes(secret_nums_arr)
		all_buyers_price_changes.append((changes_arr, secret_nums_arr))


	best_sequence, max_bananas = find_best_sequence(all_buyers_price_changes)

	print('max bananas', max_bananas)

if __name__ == '__main__':
	main()