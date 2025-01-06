import copy

def func(grid, moves, start):

	rows, cols = len(grid), len(grid[0])
	dt = {'<': [0,-1], '>': [0,1], '^': [-1,0] , 'v': [1,0]}
	x,y = start
	for mv in moves:
		new_x, new_y = x + dt[mv][0], y + dt[mv][1]
		if new_x == 0 or new_x == rows-1 or new_y == 0 or new_y == cols-1:
			continue 

		if grid[new_x][new_y] == '#':
			continue

		elif grid[new_x][new_y] == '.':
			grid[x][y] = '.'
			x, y = new_x, new_y
			grid[x][y] = '@'

		else: 
			nxt = grid[new_x][new_y]
			while 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == nxt:
				new_x += dt[mv][0]
				new_y += dt[mv][1]

			
			if new_x == 0 or new_x == rows-1 or new_y == 0 or new_y == cols-1:
				# no space between block and wall
				continue
			else:
				if grid[new_x][new_y] == '#':
					continue
				else:
					if grid[new_x][new_y] == '.':
						# move the block
						grid[new_x][new_y] = nxt
						grid[x][y] = '.'
						x, y = x + dt[mv][0], y + dt[mv][1]
						grid[x][y] = '@'
						

		# print('new grid')
		# for g in grid:
		# 	print(''.join(g))

	return grid

def main():
	grid = []
	moves = ''
	start = []
	with open('input.txt') as file:
		lines = file.readlines()
		idx = 0
		for line in lines:
			idx +=1 
			line = line.strip()
			if len(line)  == 0:
				break
			chs = [ch for ch in line]
			grid.append(chs)

		for li in range(idx, len(lines)):
			moves += lines[li].strip()

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '@':
				start = [i,j]

	final_grid = func(grid, moves,start)
	print('final grid')
	for g in final_grid:
		print(''.join(g))

	rows, cols = len(final_grid), len(final_grid[0])
	res = 0
	for i in range(rows):
		for j in range(cols):
			if final_grid[i][j] not in ['#', '.', '@']:
				res += i * 100 + j
	print('res', res)
if __name__ == '__main__':
	main()