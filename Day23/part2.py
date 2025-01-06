from collections import defaultdict

def find_max_set(graph):
	keys = list(graph.keys())
	keys.sort()
	idx = 0 

	queue = []

	for p2 in graph[keys[idx]]: # node p and its set 
		st = [keys[idx], p2]
		st.sort()
		queue.append(st)

	maxSet = queue[:]
	maxSetCnt = 2
	idx +=1 

	while idx < len(keys):
		new_queue = []
		
		p = keys[idx]
			
		new_queue.append([p]) # just node p 

		for p2 in graph[p]: # node p and its set 
			st = [p, p2]
			st.sort()
			new_queue.append(st)

		for ls in queue:
			if p in ls:
				continue

			edges = 0
			for node in ls:
				if p in graph[node]:
					edges +=1

			if edges == len(ls):
				new_ls = ls[:]
				new_ls.append(p)
				new_ls.sort()

				if maxSetCnt < len(new_ls):
					maxSet = [new_ls[:]]
					maxSetCnt = len(new_ls)

				elif maxSetCnt == len(new_ls):
					if new_ls not in maxSet:
						maxSet.append(new_ls)
				# print('maxSetCnt', maxSetCnt)
				new_queue.append(new_ls)

			new_queue.append(ls)

		idx  +=1 
		queue = new_queue

	return maxSet	

def main():
	graph = defaultdict(set)
	with open('input.txt') as file:
		for line in file: 
			line = line.strip()
			line = line.replace('-', ' ')
			xs = line.split()
			graph[xs[0]].add(xs[1])
			graph[xs[1]].add(xs[0])

	# print('graph', graph)

	maxSet = find_max_set(graph)
	print('maxSet', maxSet)


if __name__ == '__main__':
	main()