from collections import defaultdict

def find_set_of_three(graph):
	three_sets = []
	keys = list(graph.keys())
	keys.sort()

	for i in range(len(keys)):
		p1 = keys[i]
	
		for j in range(i+1, len(keys)):
			p2 = keys[j]
	
			for k in range(j+1, len(keys)):
				p3 = keys[k]
	
				if p1 in graph[p2] and p2 in graph[p3] and p3 in graph[p1]:
					three_sets.append((p1,p2,p3))
	
	return three_sets

def main():
	graph = defaultdict(list)
	with open('input.txt') as file:
		for line in file: 
			line = line.strip()
			line = line.replace('-', ' ')
			xs = line.split()
			graph[xs[0]].append(xs[1])
			graph[xs[1]].append(xs[0])
	# print('graph', graph)

	three_sets = find_set_of_three(graph)

	cnt = 0
	for st in three_sets:
		if st[0][0] == 't' or st[1][0] == 't' or st[2][0] == 't':
			cnt += 1 
			# print(st)
	print('cnt', cnt)


if __name__ == '__main__':
	main()