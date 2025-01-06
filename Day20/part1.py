from collections import defaultdict
import sys

sys.setrecursionlimit(10000)  # Set the new recursion limit

def baseDFS(grid, start):
	base = 0
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0], [0,1], [1,0], [0,-1]]

	def DFS(i,j, time):
		nonlocal base

		if i < 0 or i >= rows or j < 0 or j >= cols:
			return 

		if grid[i][j] == 'E':
			base = time
			return 

		if grid[i][j] == 'O':
			return

		if grid[i][j] in ['S', '.']:
			grid[i][j] = '0'
			for di, dj in dirs:
				new_i, new_j = i + di, j + dj
				if 0 <= new_i < rows and 0 <= new_j < cols:
					DFS(new_i, new_j, time+1)
			grid[i][j] = '.'
		return

	DFS(start[0], start[1], 0)
	return base


def funcDFS(grid, start, k):
	base = 0
	better_than_base = 0
	better_than_base_dt = defaultdict(int)
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0], [0,1], [1,0], [0,-1]]


	def DFS(i,j,k,time):
		nonlocal base
		nonlocal better_than_base

		if i < 0 or i >= rows or j < 0 or j >= cols:
			return 

		if grid[i][j] == 'E':
			# print('reach E after', time)
			better_than_base_dt[base - time] +=1
			if base - time >= 100:
				better_than_base +=1 
			return time

		if grid[i][j] == 'O':
			return

		if (grid[i][j] in ['S', '.']):
			grid[i][j] = '0'
			for di, dj in dirs:
				new_i, new_j = i + di, j + dj
				if 0 <= new_i < rows and 0 <= new_j < cols:
					DFS(new_i, new_j, k, time + 1)
			grid[i][j] = '.'

		if grid[i][j] == '#' and k != 0:
			grid[i][j] = '0'
			for di, dj in dirs:
				new_i, new_j = i + di, j + dj
				if 0 <= new_i < rows and 0 <= new_j < cols:
					DFS(new_i, new_j, k - 1, time + 1)
			grid[i][j] = '#'
		return

	base = baseDFS(grid, start)
	print('base', base)
	DFS(start[0], start[1], k, 0)
	print('better_than_base_dt')
	keys = list(better_than_base_dt.keys())
	keys.sort()
	for k in keys:
		print(better_than_base_dt[k], 'cheats', k , 'picoseconds')
	return better_than_base

def baseBFS(grid, start):
	base = 0
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0], [0,1], [1,0], [0,-1]]

	queue = []
	queue.append((start[0], start[1], 0))
	visited = set()

	while len(queue) > 0:
		i, j, time = queue.pop(0)
		if (i,j) in visited:
			continue 

		visited.add((i,j))
		if grid[i][j] == 'E':
			base = time
			continue

		if grid[i][j] == '.' or grid[i][j] == 'S':
			for di, dj in dirs:
				new_i, new_j = i + di, j + dj
				if 0 <= new_i < rows and 0 <= new_j < cols:
					queue.append((new_i, new_j, time + 1))

	return base

def funcBFS(grid, start, k):
	base = baseBFS(grid, start)
	print('baseBFS', base)

	better_than_base = 0
	better_than_base_dt = defaultdict(int)
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0], [0,1], [1,0], [0,-1]]

	queue = []
	queue.append((start[0], start[1], k, 0, []))
	# visited = set()
	while len(queue) > 0:
		print('len queue', len(queue))
		i, j, cur_k, time, path = queue.pop(0)

		if time - base >= 100:
			continue

		if (i,j) in path:
			continue

		if grid[i][j] == 'E':
			print('reach End in', time, 'picoseconds')
			better_than_base_dt[base - time] +=1 
			if base - time >= 100:
				better_than_base +=1 
			continue

		if grid[i][j] == '.' or grid[i][j] == 'S':
			for di, dj in dirs:
				new_i, new_j = i + di, j + dj
				if 0 <= new_i < rows and 0 <= new_j < cols:
					queue.append((new_i, new_j, cur_k, time + 1, path + [(i,j)] ))
			continue

		if grid[i][j] == '#':
			if cur_k == 0:
				continue
			for di, dj in dirs:
				new_i, new_j = i + di, j + dj
				if 0 <= new_i < rows and 0 <= new_j < cols:
					queue.append((new_i, new_j, cur_k-1, time + 1, path + [(i,j)] ))
			continue

	print('better_than_base_dt')
	keys = list(better_than_base_dt.keys())
	keys.sort()
	for k in keys:
		print(better_than_base_dt[k], 'cheats', k , 'picoseconds')
	return better_than_base

def main():
	grid = []
	start, end = [], []

	with open('sample.txt') as file:
		for line in file:
			grid.append(list(line.strip()))

	# print('grid')
	# for row in grid:
	# 	print(''.join(row))

	rows, cols = len(grid), len(grid[0])

	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == 'S':
				start = [i,j]
			if grid[i][j] == 'E':
				end = [i,j]

	hundred_secs_saved = funcBFS(grid, start, 1)
	print('hundred_secs_saved', hundred_secs_saved)

if __name__ == '__main__':
	main()

