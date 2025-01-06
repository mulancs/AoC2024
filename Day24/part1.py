from collections import defaultdict

def func(states, wires, in_orders):

	while len(in_orders) > 0:
		# print('in_orders', in_orders)
		zero_ins = set()
		nodes = in_orders.items()
		for node, val in nodes:
			if val == 0:
				zero_ins.add(node)
				del in_orders[node]

		if len(zero_ins) == 0:
			break

		for node1 in zero_ins:
			ls = wires[node1]
			for op, node2, output in ls:
				if node2 not in zero_ins:
					continue

				ans = 0
				if op == 'AND':
					ans = states[node1] & states[node2]
				elif op == 'OR':
					ans = states[node1] | states[node2]
				elif op == 'XOR':
					ans = states[node1] ^ states[node2]

				print('calculate', output, ans)
				states[output] = ans

				wires[node1].remove((op, node2, output))
				wires[node2].remove((op, node1, output))

				in_orders[output] -= 2

	return states

def main():
	states = defaultdict(int)
	wires = defaultdict(list)
	in_orders = defaultdict(int)

	with open('sample.txt') as file:
		for line in file:
			line = line.strip()
			if len(line) == 0:
				continue
			if ':' in line:
				ws = line.split(':')
				states[ws[0]] = int(ws[1])
				in_orders[ws[0]] = 0 

			if '-' in line:
				ws = line.split()
				input1, op, input2, output = ws[0], ws[1], ws[2], ws[4]
				wires[input1].append((op, input2, output))
				wires[input2].append((op, input1, output))
				in_orders[output] += 2

	# print('states', states)
	# print('wires', wires)
	# print('in_orders', in_orders)

	final_states = func(states, wires, in_orders)
	# print('final_states', final_states)
	print('final_states')
	keys = list(final_states.keys())
	keys.sort()
	for k in keys:
		print(k, ':', final_states[k])

	z_keys = []
	for k in keys:
		if k[0] == 'z':
			z_keys.append(k)

	z_keys.sort()
	ans = 0
	idx = 0 
	print('z_keys', z_keys)
	for zk in z_keys:
		ans += states[zk] * pow(2,idx)
		idx +=1
	print('ans', ans) 


if __name__ == '__main__':
	main()