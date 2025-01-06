import copy 

SIZE = 71
NUM_PTS = 1024
dirs = [[-1, 0], [0,1], [1,0], [0,-1]]

def DFS(grid):

	minPath = float('inf')
	rows = SIZE
	cols = SIZE


	def recursion(i,j, cnt):
		nonlocal minPath

		if i < 0 or i >= rows or j < 0 or j >= cols:
			return 

		if i == rows - 1 and j == cols - 1:
			minPath = min(minPath, cnt)
			print('Done', cnt)
			return 

		if grid[i][j] == '#':
			return

		grid[i][j] = '#'
		for di, dj in dirs:
			recursion(i + di, j + dj, cnt + 1)

		grid[i][j] = '.'
		return 

	recursion(0,0,0)

	return minPath

def BFS(grid):
	minPath = float('inf')
	rows, cols = SIZE, SIZE 
	visited = set()
	queue = [(0,0,0)]

	while len(queue) > 0:
		x, y, cnt = queue.pop(0)

		if x == rows - 1 and y == cols - 1:
			minPath = min(minPath, cnt)
			print('Done', cnt, 'minPath', minPath)
			continue

		if (x,y) in visited:
			continue

		visited.add((x,y))

		for dx, dy in dirs:
			new_x, new_y = x + dx, y + dy
			if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '.':
				queue.append((new_x, new_y, cnt+1))

	return minPath

def func(pts):
	rows = SIZE
	cols = SIZE

	grid = [['.' for _ in range(cols)] for _ in range(rows)]

	for i in range(NUM_PTS):
		x, y = pts[i][0], pts[i][1]
		grid[x][y] = '#'

	# for line in grid:
	# 	print(''.join(line))

	return BFS(grid)

def main():
	pts = []
	with open('input.txt') as file:
		for line in file:
			nums = line.strip().split(',')
			pts.append([int(nums[1]), int(nums[0])])
	print(func(pts))

if __name__ == '__main__':
	main()