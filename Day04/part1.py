def part1(words):
	xmas, samx = 'XMAS', 'SAMX'
	cnt = 0
	rows, cols = len(words), len(words[0])
	# row 
	for w in words:
		for i in range(cols -3):   # last one = cols-4, -3, -2, cols-1
			if w[i:i+4] == xmas or w[i:i+4] == samx:
				cnt +=1 

	# cols 
	for col in range(cols):
		for i in range(rows-3):
			down = ''
			for j in range(4):
				down += words[i+j][col]
			if down == xmas or down == samx:
				cnt +=1 

	# diagonal 
	for i in range(rows):
		for j in range(cols):
			diagonal = ''
			for k in range(4):
				new_i, new_j = i + k, j + k
				if 0 <= new_i < rows and 0 <= new_j < cols:
					diagonal += words[new_i][new_j]
					if diagonal == xmas or diagonal == samx:
						cnt += 1 
				else:
					break

	# anti-diagonal 
	for i in range(rows):
		for j in range(cols-1, -1, -1):
			anti_diagonal = ''
			for k in range(4):
				new_i, new_j = i + k, j - k
				if 0 <= new_i < rows and 0 <= new_j < cols:
					anti_diagonal += words[new_i][new_j]
					if anti_diagonal == xmas or anti_diagonal == samx:
						cnt += 1 
				else:
					break

	return cnt

def main():
	words = []
	with open('input.txt') as file:
		for line in file:
			words.append(line.strip())
	print(part1(words))

if __name__ == '__main__':
	main()