import sys
from collections import defaultdict

sys.setrecursionlimit(10000)  # Set the new recursion limit

def func1(grid, start, end):
	print('start', start, 'end', end)
	minScore = float('inf')
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0],[0,1],[1,0],[0,-1]]
	ds = [1, 3]
	visited = [ [float('inf')] * cols for _ in range(rows)]
	prevs = [ [set() for _ in range(cols)] for _ in range(rows)]

	def recursion(prev_i, prev_j, prev_d, i,j, d, cnt):
		nonlocal minScore

		if i == 7 and j == 3:
			print('visit i = 7 and j = 3', 'sym =', grid[i][j], 'cnt =', cnt)

		if i == 7 and j == 4:
			print('visit i = 7 and j = 4', 'sym =', grid[i][j], 'cnt =', cnt)


		if i < 0 or i >= rows or j < 0 or j >= cols:
			return 

		if grid[i][j] == '#': 
			return 

		if cnt > visited[i][j]:
			if i == 7 and j == 3:
				print('case 1')
			return 

		elif cnt == visited[i][j]:
			if i == 7 and j == 3:
				print('case 2')
			prevs[i][j].add((prev_i, prev_j))

		elif cnt < visited[i][j]:
			if i == 7 and j == 3:
				print('case 3')

			visited[i][j] = cnt
			prevs[i][j].clear()
			prevs[i][j].add((prev_i, prev_j))		

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
	queue = [(end[0],end[1])]

	print('queue', queue)
	print('cnt', visited[8][3],'at i = 8 j = 3', prevs[8][3])
	print('cnt', visited[7][3],'at i = 7 j = 3', prevs[7][3])
	print('cnt', visited[7][3],'at i = 7 j = 3', prevs[7][3])
	print('cnt', visited[7][4],'at i = 7 j = 4', prevs[7][4])
	print('cnt', visited[7][5],'at i = 7 j = 5', prevs[7][5])

	while len(queue) > 0:
		cur = queue.pop()
		if cur in cells:
			continue
		cells.add(cur)

		for prev in prevs[cur[0]][cur[1]]:
			queue.append(prev)

	for x,y in cells:
		grid[x][y] = '0'

	print('grid')
	for line in grid:
		print(''.join(line))
	return len(cells)


################################################################

def DFS(grid, start, end):
	print('start', start, 'end', end)
	minScore = float('inf')
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0],[0,1],[1,0],[0,-1]]
	ds = [1, 3]
	final_path = []

	def recursion(i,j, d, cnt, path):
		nonlocal minScore
		if i < 0 or i >= rows or j < 0 or j >= cols:
			return 

		if grid[i][j] == '#': 
			return 

		if grid[i][j] == 'E':
			print('found E', minScore)

			if cnt > minScore:
				return

			elif cnt < minScore:
				final_path.clear()
				final_path.append(path)
				minScore = cnt

			elif cnt == minScore:
				final_path.append(path)
			return 

		if (i,j,d) in path:
			return

		recursion(i + dirs[d][0], j + dirs[d][1], d, cnt+1, path + [(i,j,d)])

		for k in ds:
			new_d = (d + k) % 4
			new_i, new_j = i + dirs[new_d][0], j + dirs[new_d][1]
			recursion(new_i, new_j, new_d, cnt+1000+1,path + [(i,j,d)])
		
		return 

	recursion(start[0], start[1], 1, 0, [])
	print(minScore)
	cells = set()
	for path in final_path:
		for c in path:
			cells.add((c[0], c[1]))

	for x,y in cells:
		grid[x][y] = '0'

	print('grid')
	for line in grid:
		print(''.join(line))
	return len(cells)

################################################################

def BFS(grid, start, end):
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0],[0,1],[1,0],[0,-1]]
	ds = [1, 3]

	visited = set()
	queue = []
	queue.append(start)
	path = defaultdict(list)

	while len(queue) > 0:
		cur = queue.pop(0)
		if cur == end or grid[cur[0]][cur[1]] == '#':
			continue
		if cur in visited:
			continue
		visited.add(cur)

		for dx, dy in ds:
			new_x, new_y = cur[0] + dx, cur[1] + dy
			if 0 <= new_x < rows and 0 <= new_y < cols:
				if grid[new_x][new_y] == '.' and (new_x, new_y) not in visited:
					queue.append((new_x, new_y))
					path[(new_x, new_y)].append((cur[0], cur[1]))

	cells = set()
	queue =  [(end[0], end[1])]
	while cur != (start[0], start[1]):
		cells.add(cur)
		f


def main():
	grid = []
	with open('input.txt') as file:
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
	
	print(BFS(grid, start, end))

if __name__ == '__main__':
	main()