import copy 
import sys

sys.setrecursionlimit(100000)

grids = []
rows, cols = 0, 0
dirs = [[-1,0], [0,1], [1,0], [0,-1]]
start = [0,0]
candidates = []

def recursion(r, c, d, path, new_grids):
	if (r,c, d % 4) in path:
		return True
	new_path = copy.deepcopy(path)
	new_path.add((r,c,d % 4))

	next_r, next_c = r + dirs[d%4][0], c + dirs[d%4][1]
	
	if next_r >= rows or next_c >= cols or next_r < 0 or next_c < 0:
		return False
	if (next_r, next_c, d % 4) in new_path:
		return True 

	if new_grids[next_r][next_c] not in ['#', '0']:
		return recursion(next_r, next_c, d % 4, new_path, new_grids)
	else:
		new_r, new_c = r + dirs[(d+1)%4][0], c + dirs[(d+1)%4][1]

		if 0 <= new_r < rows and 0 <= new_c < cols:
			if (new_r, new_c, (d+1)% 4) in new_path:
				return True 
			if new_grids[new_r][new_c] not in ['#', '0']:
				return recursion(new_r, new_c, (d + 1) % 4, new_path, new_grids) 

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
		elif grids[i][j] == '.':
			candidates.append((i,j))

# print('candidates', candidates)
pos = []
for i,j in candidates:
	# print('check', 'i', i, 'j', j)
	new_grids = copy.deepcopy(grids)
	new_grids[i][j] = '0'

	if recursion(start[0], start[1], 0, set(), new_grids):
		print('pos', i,j)
		pos.append((i,j))
		for line in new_grids:
			print(''.join(line))

print('final', len(pos))