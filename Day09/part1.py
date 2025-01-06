
input_str = ''
with open('input.txt') as file:
	for line in file:
		input_str = line.strip()

disk = []
file_or_space = 0 
cur_file_idx = 0

for ch in input_str:
	if file_or_space == 0:
		disk += [str(cur_file_idx)] * int(ch)
		file_or_space +=1 
		cur_file_idx +=1 

	elif file_or_space == 1:
		disk += ['.'] * int(ch)
		file_or_space = 0

print('disk', disk)

# two pointers 
fs = []
p1, p2 = 0, len(disk) -1
while p1 < len(disk) and p2 > p1:
	if disk[p1] != '.':
		fs.append(disk[p1])
		p1 +=1 
	else:
		while p2 > p1 and disk[p2] == '.':
			p2 -=1 
		if disk[p2] != '.':
			fs.append(disk[p2])
			disk[p2] = '.'
			p1 +=1
print('fs',''.join(fs))

checksum = 0
for i, ch in enumerate(fs):
	if ch == '.':
		break
	checksum += i * int(ch)

print('checksum', checksum)