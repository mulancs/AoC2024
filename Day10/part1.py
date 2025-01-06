grid = []
trailheads = []
dirs = [[1,0],[-1,0],[0,1],[0,-1]]

def recursion_helper(x, y, rows, cols):
	score = set()
	
	def recursion(r,c,rows,cols):
		nonlocal score
		if r < 0 or r == rows or c < 0 or c == cols:
			return 

		if grid[r][c] == '9':
			score.add((r,c))
			# print('r','c', r, c)
			return

		for dx, dy in dirs:
			new_r, new_c = r + dx, c + dy
			if 0 <= new_r < rows and 0 <= new_c < cols and int(grid[new_r][new_c]) - int(grid[r][c]) == 1:
				recursion(new_r, new_c, rows, cols)

	recursion(x,y, rows, cols)
	return len(score)

def func():
	scores = 0
	rows, cols = len(grid), len(grid[0])
	for start in trailheads:
		# print('start', start)
		score = recursion_helper(start[0], start[1], rows, cols)
		# print('score', score)
		scores += score
	return scores

def process_input(filename):
	with open(filename) as file:
		line_idx = 0
		for line in file:
			line = line.strip()
			nums = []
			col_idx = 0
			for ch in line:
				nums.append(ch)
				if ch == '0':
					trailheads.append((line_idx, col_idx))
				col_idx += 1
			line_idx +=1 
			grid.append(nums)

def main():
	process_input('input.txt')
	print(func())

if __name__ == '__main__':
	main()