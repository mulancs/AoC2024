import sys

sys.setrecursionlimit(10000)  # Set the new recursion limit

def func(grid, start):

	minScore = float('inf')
	rows, cols = len(grid), len(grid[0])
	dirs = [[-1,0],[0,1],[1,0],[0,-1]]
	ds = [1, 3]
	visited = {}

	def recursion(i,j, d, cnt):
		nonlocal minScore
	
		if i < 0 or i >= rows or j < 0 or j >= cols:
			return 

		if grid[i][j] == 'E':
			minScore = min(minScore, cnt)
			print('found E', minScore)
			return 

		if grid[i][j] == '#': 
			return 

		if (i,j,d) in visited:
			if cnt >= visited[(i,j,d)]:
				return 

		visited[(i,j,d)] = cnt

		recursion(i + dirs[d][0], j + dirs[d][1], d, cnt+1)

		for k in ds:
			new_d = (d + k) % 4
			new_i, new_j = i + dirs[new_d][0], j + dirs[new_d][1]
			recursion(new_i, new_j, new_d, cnt+1000+1)
		
		return 

	recursion(start[0], start[1], 1, 0)
	return minScore


def main():
	grid = []
	with open('input.txt') as file:
		for line in file:
			line = line.strip()
			s = []
			for ch in line:
				s.append(ch)
			grid.append(s)

	start = [0,0]
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 'S':
				start = [i,j]
				break
	print(func(grid, start))

if __name__ == '__main__':
	main()