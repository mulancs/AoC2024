import copy 

SIZE = 71

dirs = [[-1, 0], [0,1], [1,0], [0,-1]]

def BFS(grid):
	rows, cols = SIZE, SIZE 
	visited = set()
	queue = [(0,0,0)]
	while len(queue) > 0:
		x, y, cnt = queue.pop(0)

		if x == rows - 1 and y == cols - 1:
			print('Done', cnt)
			return True

		if (x,y) in visited:
			continue

		visited.add((x,y))

		for dx, dy in dirs:
			new_x, new_y = x + dx, y + dy
			if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '.':
				queue.append((new_x, new_y, cnt+1))

	return False

def func(pts):
	rows = SIZE
	cols = SIZE

	grid = [['.' for _ in range(cols)] for _ in range(rows)]

	for i in range(len(pts)):
		x, y = pts[i][0], pts[i][1]
		grid[x][y] = '#'
		if not BFS(grid):
			return pts[i]

def main():
	pts = []
	with open('input.txt') as file:
		for line in file:
			nums = line.strip().split(',')
			pts.append([int(nums[1]), int(nums[0])])
	print(func(pts))

if __name__ == '__main__':
	main()