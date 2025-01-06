dirs = [[1,0],[-1,0],[0,1],[0,-1]]

def func(grid):
	print('grid', grid)
	rows, cols = len(grid), len(grid[0])
	visited = set()
	price = 0

	for i in range(rows):
		for j in range(cols):
			if (i,j) in visited:
				continue 

			boundary_edge_cnt = 0
			neighbor_cells = 0 
			type = grid[i][j]

			queue = []	
			queue.append((i,j))
			
			while len(queue) > 0:
				cur_i, cur_j = queue.pop()
				if (cur_i, cur_j) in visited:
					continue

				visited.add((cur_i,cur_j))
				neighbor_cells += 1 

				for di, dj in dirs:
					new_i, new_j = cur_i + di, cur_j + dj
					if 0 <= new_i < rows and 0 <= new_j < cols:
						if grid[new_i][new_j] == type:
							if (new_i, new_j) not in visited:
								queue.append((new_i, new_j))
						else:
							boundary_edge_cnt += 1
					else:
						boundary_edge_cnt += 1
			print('type', type, 'edges', boundary_edge_cnt, 'cells', neighbor_cells)

			price += boundary_edge_cnt * neighbor_cells

	return price


def main():
	grid = []
	with open('input.txt') as file:
		for line in file:
			line = line.strip()
			l = []
			for ch in line:
				l.append(ch)
			grid.append(l)
	print(func(grid))


if __name__ == '__main__':
	main()