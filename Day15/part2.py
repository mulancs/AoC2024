import copy

def func(grid, moves, start):

	rows, cols = len(grid), len(grid[0])
	dt = {'<': [0,-1], '>': [0,1], '^': [-1,0] , 'v': [1,0]}
	nbs = [[0,-1], [0,1], [-1,0], [1,0]]
	boxes = ['[', ']']
	x,y = start

	for mv in moves:
		print('move', mv)
		new_x, new_y = x + dt[mv][0], y + dt[mv][1]
		if new_x == 0 or new_x == rows or new_y == 0 or new_y == cols:
			continue 

		if grid[new_x][new_y] == '#':
			continue

		elif grid[new_x][new_y] == '.':
			grid[x][y] = '.'
			x, y = new_x, new_y
			grid[x][y] = '@'

		elif grid[new_x][new_y] in boxes and mv == '<' or mv == '>':
			# if there's space 
			neighbors = []
			neighbors.append((new_x, new_y, grid[new_x][new_y]))
			next_x, next_y = new_x + dt[mv][0], new_y + dt[mv][1]
			while 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] in boxes:
				neighbors.append((next_x, next_y, grid[next_x][next_y]))
				next_x, next_y =  next_x + dt[mv][0], next_y + dt[mv][1]

			if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] == '#':
				continue 

			neighbors = neighbors[::-1]
				
			for nbx, nby, sym in neighbors:
				new_nbx, new_nby = nbx + dt[mv][0], nby + dt[mv][1]
				grid[new_x][new_nby] = sym
				grid[nbx][nby] = '.'
			grid[new_x][new_y] = '@' 
			grid[x][y] = '.'
			x, y = new_x, new_y

		elif grid[new_x][new_y] in boxes and mv == '^' or mv == 'v':
			neighbors = [[new_x, new_y, grid[new_x][new_y]]]

			if grid[new_x][new_y] == '[':
				neighbors.append([new_x, new_y + 1 , ']'])
			elif grid[new_x][new_y] == ']':
				neighbors.append([new_x, new_y - 1, '['])
			
			queue = neighbors[:]
			neighbors = []
			no_space = False
			while len(queue) > 0:
				print('queue', queue)
				new_queue = []

				for cell in queue:
					cur_x, cur_y, sym = cell
					neighbors.append(cell)
					next_x, next_y = cur_x + dt[mv][0], cur_y + dt[mv][1]
					
					if 0 < next_x < rows and 0 < next_y < cols:
						if grid[next_x][next_y]  == '[':
							new_queue.append([next_x, next_y, '['])
							new_queue.append([next_x, next_y + 1, ']'])
						elif grid[next_x][next_y] == ']':
							new_queue.append([next_x, next_y, ']'])
							new_queue.append([next_x, next_y - 1,'['])
						elif grid[next_x][next_y] == '#':
							no_space = True
							break
					else:
						no_space = True
						break

				queue = new_queue

			if no_space:
				continue

			print('found neighbors', neighbors)
			if mv == '^':
				neighbors.sort()

			for nbx, nby, sym in neighbors:
				print(nbx, nby, sym)
				new_nbx, new_nby = nbx + dt[mv][0], nby + dt[mv][1]
				print('new', new_nbx, new_nby, sym)
				grid[new_nbx][new_nby] = sym
				grid[nbx][nby] = '.'

			grid[new_x][new_y] = '@' 
			grid[x][y] = '.'
			x, y = new_x, new_y


		print('new grid')
		for g in grid:
			print(''.join(g))

	return grid

def main():
	grid = []
	moves = ''
	start = []
	with open('large_sample.txt') as file:
		lines = file.readlines()
		idx = 0
		for line in lines:
			idx +=1 
			line = line.strip()
			if len(line)  == 0:
				break
			chs = []
			for ch in line:
				if ch == '#':
					chs.extend(['#', '#'])
				elif ch == 'O':
					chs.extend(['[', ']'])
				elif ch == '.':
					chs.extend(['.', '.'])
				elif ch == '@':
					chs.extend(['@', '.'])

			grid.append(chs)

		for li in range(idx, len(lines)):
			moves += lines[li].strip()

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '@':
				start = [i,j]

	print('original grid')
	for g in grid:
		print(''.join(g))

	final_grid = func(grid, moves,start)
	print('final grid')
	for g in final_grid:
		print(''.join(g))

	rows, cols = len(final_grid), len(final_grid[0])
	res = 0
	for i in range(rows):
		for j in range(cols):
			if final_grid[i][j] == '[':
				res += i * 100 + j
	print('res', res)


if __name__ == '__main__':
	main()