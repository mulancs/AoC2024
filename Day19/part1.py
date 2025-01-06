def build_trie(colors):
	trie = {'.': {}}

	cur = trie['.']
	
	for clr in colors:
		for ch in clr:
			if ch not in cur:
				cur[ch] = {}
			cur = cur[ch]
		cur['$'] = {}
		cur = trie['.']

	return trie 


def find_match(trie, ptn):
	ws = []
	node = trie['.']
	cur = ''
	for ch in ptn:
		# print('char', ch)
		if ch in node:
			cur += ch
			node = node[ch]
			# print('cur', cur, 'node', node)
			if '$' in node:
				ws.append(cur)
		else:
			return ws
	return ws


def validate(trie, ptn):
	# print('validate ', ptn)
	if ptn == '':
		return True 

	ws = find_match(trie, ptn)
	# print('potential_ws', ws)

	match = False

	for w in ws:
		match = match or validate(trie, ptn[len(w):])

	return match

def func(trie, patterns):

	# patterns = ['bwurrg']
	cnt = 0
	for ptn in patterns:
		if validate(trie, ptn):
			print('pattern', ptn)
			cnt +=1 
	return cnt


def main():
	colors = []
	patterns = []

	with open('input.txt') as file:
		line = file.readline()
		colors = line.split()
		colors = [x.strip(',') for x in colors]
		colors.sort()
		file.readline()
		while True:
			line = file.readline()
			if not line:
				break

			patterns.append(line.strip())

	print('colors', colors)
	print('patterns', patterns)

	trie = build_trie(colors)
	print(trie)

	cnt = func(trie, patterns)
	print('cnt', cnt)

if __name__ == '__main__':
	main()