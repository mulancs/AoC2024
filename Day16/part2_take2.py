import sys

sys.setrecursionlimit(10000)  # Set the new recursion limit

def func(grid, start, end):

	minScore = float('inf')
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0],[0,1],[1,0],[0,-1]]
	ds = [1, 3]
	visited = {}

	def recursion(prev_i, prev_j, prev_d, i,j, d, cnt):
		nonlocal minScore
	
		if i < 0 or i >= rows or j < 0 or j >= cols:
			return 

		if grid[i][j] == '#': 
			return 

		if (i,j,d) in visited:
			if cnt > visited[(i,j,d)][0]:
				return 
			if cnt == visited[(i,j,d)][0]:
				visited[(i,j,d)][1].add((prev_i, prev_j, prev_d))
			
			elif cnt < visited[(i,j,d)][0]:
				s = set()
				s.add((prev_i, prev_j, prev_d))
				visited[(i,j,d)] = [cnt,s]
		else:
			s = set()
			s.add((prev_i, prev_j, prev_d))
			visited[(i,j,d)] = [cnt, s]

		if grid[i][j] == 'E':
			minScore = min(minScore, cnt)
			print('found E', minScore)
			return 
		
		recursion(i,j,d, i + dirs[d][0], j + dirs[d][1], d, cnt+1)

		for k in ds:
			new_d = (d + k) % 4
			new_i, new_j = i + dirs[new_d][0], j + dirs[new_d][1]
			recursion(i,j,d, new_i, new_j, new_d, cnt+1000+1)
		
		return 

	recursion(start[0], start[1], 1, start[0], start[1], 1, 0)
	print(minScore)

	cells = set()
	queue = []
	for d in [0,1,2,3]:
		if (end[0], end[1], d) in visited:
			queue.append((end[0], end[1],d))

	print('queue', queue)
	while len(queue) > 0:
		cur = queue.pop()
		if cur in cells:
			continue
		cells.add(cur)

		for prev in visited[cur][1]:
			queue.append(prev)

	distinct_cells = set()
	for x,y,d in cells:
		distinct_cells.add((x,y))
		grid[x][y] = '0'
	print('grid')
	for line in grid:
		print(''.join(line))
	return len(distinct_cells)

def main():
	grid = []
	with open('example1.txt') as file:
		for line in file:
			line = line.strip()
			grid.append(list(line))

	start, end = [0,0], [0,0]

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 'S':
				start = [i,j]
			if grid[i][j] == 'E':
				end = [i,j]
	
	print(func(grid, start, end))

if __name__ == '__main__':
	main()