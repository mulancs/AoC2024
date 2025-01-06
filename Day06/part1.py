import copy 
import sys

sys.setrecursionlimit(10000)

grids = []
rows, cols = 0, 0
dirs = [[-1,0], [0,1], [1,0], [0,-1]]
start = [0,0]

def recursion(r, c, d, path):
	# print('recursion', r, c, d, grids[r][c], 'path', path)

	new_path = path[:]
	new_path.append((r,c))

	next_r, next_c = r + dirs[d%4][0], c + dirs[d%4][1]
	# print('next_r', next_r, 'next_c', next_c)

	if next_r >= rows or next_c >= cols or next_r < 0 or next_c < 0:
		return new_path[:]  

	if grids[next_r][next_c] != '#':
		return recursion(next_r, next_c, d, new_path)
	else:
		new_r, new_c = r + dirs[(d+1)%4][0], c + dirs[(d+1)%4][1]
		if 0 <= new_r < rows and 0 <= new_c < cols:
			if grids[new_r][new_c] != '#':
				return recursion(new_r, new_c, d + 1, new_path) 


with open('input.txt') as file:
	for line in file:
		line = line.strip()
		l = []
		for ch in line:
			l.append(ch)
		grids.append(l)

rows, cols = len(grids), len(grids[0])
for i in range(rows):
	for j in range(cols):
		if grids[i][j] == '^':
			start = [i,j]
			break

path = recursion(start[0], start[1], 0, [])
print('len path', len(set(path)))
