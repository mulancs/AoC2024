import re 

def part1_regex(text):
	pattern = r"mul\([0-9]+,[0-9]+\)"

	search = re.finditer(pattern, text)
	sm = 0
	previous_end = 0
	for match in search:
		m = text[match.start():match.end()]

		num1, num2 = '', ''
		i = 4
		while i < len(m) and m[i].isdigit():
			num1 += m[i]
			i += 1
		i += 1
		while i < len(m) and m[i].isdigit():
			num2 += m[i]
			i += 1
		if int(num1) >= 1000 or int(num2) >= 1000:
			continue 

		print('check from', text[previous_end:match.start()], 'before', m)
		sch = text[previous_end:match.start()]
		if "do()" not in sch and "don\'t()" not in sch:
			print('num1', num1, 'num2', num2)
			sm += int(num1) * int(num2)
			previous_end = match.end()
			continue 
		else:		
			for i in range(len(sch)-1, -1, -1):
				if "do()" in sch[i:]:
					print('num1', num1, 'num2', num2)
					sm += int(num1) * int(num2)
					previous_end = match.end()
					break
				elif "don\'t()" in sch[i:]:
					break

	return sm

def part1(text):
	pairs = []
	i = 0
	while i < len(text) - 3:
		if text[i:i+3] == 'mul':
			i = i + 3
			if text[i] == '(':
				i +=1 
				num1 = ''
				for _ in range(3):
					if text[i].isdigit():
						num1 += text[i]
						i +=1 
					else:
						break

				if num1 != '' and text[i] == ',':
					num2 = '' 
					i +=1
					for _ in range(3):
						if text[i].isdigit():
							num2 += text[i]
							i +=1 
						else:
							break
					if text[i] == ')':
						pairs.append((num1, num2))

		i += 1

	res = 0
	for x, y in pairs:
		res += int(x) * int(y) 
	return res

def main():
	total_sum = 0
	with open('input.txt') as file:
		for line in file:
			s = part1_regex(line)
			print('s', s)
			total_sum += s
	print('total_sum', total_sum)
	
if __name__ == '__main__':
	main()