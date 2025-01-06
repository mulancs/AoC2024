rows, cols = 103, 101 
# rows, cols = 7, 11

def func(pos, vel):
	sec = 0 
	while sec < 100:
		new_pos = []
		for idx in range(len(pos)):
			i, j = pos[idx][0], pos[idx][1]
			pi, pj = i + vel[idx][0], j + vel[idx][1]

			if pi < 0:
				pi += rows
			if pi >= rows:
				pi -= rows
			if pj < 0:
				pj += cols
			if pj >= cols:
				pj -= cols

			# print('idx', idx, 'old', pos[idx], 'new', [pi, pj])
			new_pos.append([pi, pj])

		pos = new_pos
		sec +=1

	print('pos', pos)
	# grid = [[0] * 11 for _ in range(rows)]
	# for i,j in pos:
	# 	grid[i][j] += 1

	# print('grid')
	# for line in grid:
	# 	print(line)

	quads = [[0, rows//2-1, 0, cols//2-1],[0, rows//2+1, cols//2+1, cols-1],
			 [rows//2+1, rows-1, 0, cols//2-1], [rows//2+1, rows-1, cols//2+1, cols-1]]

	ans = []
	for q in quads:
		cnt = 0
		minR, maxR, minC, maxC = q
		for i,j in pos:
			if minR <= i <= maxR and minC <= j <= maxC:
				cnt +=1 
		ans.append(cnt)
	print('ans',ans)
	return ans[0] * ans[1] * ans[2] * ans[3]

def main():
	pos = []
	vel = []
	with open('input.txt') as file:
		for line in file:
			ws = line.strip().split()
			ps = ws[0].replace('=', ',')
			ps = ps.split(',')
			pos.append([int(ps[2]), int(ps[1])])
			vs = ws[1].replace('=',',')
			vs = vs.split(',')
			vel.append([int(vs[2]), int(vs[1])])

	# print('pos', pos)
	# print('vel', vel)

	print(func(pos, vel)) 


if __name__ == '__main__':
	main()