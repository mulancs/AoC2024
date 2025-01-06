def part1(words):
	mas_sam = ['MAS', 'SAM']
	cnt = 0
	rows, cols = len(words), len(words[0])
	selected = set()
	for i in range(rows):
		for j in range(cols):
			if words[i][j] != 'A':
				continue

			top_left = i -1, j -1
			bottom_right = i + 1, j + 1 
			top_right = i - 1, j + 1
			bottom_left = i + 1, j - 1
			above = i-1, j
			below = i+1, j
			diagonal = ''
			if 0<= top_left[0] < rows and  0<= top_left[1] < cols and 0<= bottom_right[0] < rows and  0<= bottom_right[1] < cols:
				diagonal = words[top_left[0]][top_left[1]] + 'A' + words[bottom_right[0]][bottom_right[1]]

			anti_diagonal = ''
			if 0<= top_right[0] < rows and  0<= top_right[1] < cols and 0<= bottom_right[0] < rows and  0<= bottom_right[1] < cols:
				anti_diagonal = words[top_left[0]][top_left[1]] + 'A' + words[bottom_right[0]][bottom_right[1]]
			
			if diagonal in mas_sam and anti_diagonal in mas_sam:
				if 0 <= above[0] < rows and 0 <= above[1] < cols and 0 <= below[0] < rows and 0 <= below[1] < rows and words[above[0]][above[1]] != 'A' and words[below[0]][below[1]] != 'A':
					print('diagonal', diagonal, 'anti_diagonal', anti_diagonal)
					selected.add((i,j))
					selected.add(top_left)
					selected.add(bottom_right)
					selected.add(top_right)
					selected.add(bottom_left)
					cnt +=1 

	to_print = []
	for i in range(rows):
		this_row = ''
		for j in range(cols):
			if (i,j) in selected:
				this_row += words[i][j]
			else:
				this_row += '.'
		print(this_row)
	return cnt

def main():
	words = []
	with open('sample_input.txt') as file:
		for line in file:
			words.append(line.strip())
	print(part1(words))

if __name__ == '__main__':
	main()