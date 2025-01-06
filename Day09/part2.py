
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
# print('disk', ''.join(disk))

p1 = 0 
spaces, files = [], []
# start_offset, len, idx

while p1 < len(disk):
	if disk[p1] == '.':
		cur = '.'
		p1 +=1 
		while p1 < len(disk) and disk[p1] == '.':
			cur += disk[p1]
			p1 +=1 

		spaces.append([p1 - len(cur),len(cur)])
	else: #if disk[p1].isnumeric():
		cur = disk[p1]
		p1 +=1 
		cnt = 1
		while p1 < len(disk) and disk[p1] == cur:
			cnt += 1
			p1 +=1 
		files.append([p1 - cnt, cnt, cur])

# print('spaces', spaces)
print('files', files)

p2 = len(files) -1 
prev_file = float('inf')
while p2 >= 0:
	cur_file_idx, cur_file_len, cur_file = files[p2]
	if int(cur_file[0]) >= prev_file:
		p2 -= 1
		continue
	p1 = 0 
	while p1 < len(spaces) and spaces[p1][0] < cur_file_idx and spaces[p1][1] < cur_file_len:
		p1 +=1 

	if p1 < len(spaces) and spaces[p1][0] < cur_file_idx:
		if spaces[p1][1] == cur_file_len:
			space_idx, space_ln = spaces[p1]
			del spaces[p1]
			files[p2][0] = space_idx
		elif spaces[p1][1] > cur_file_len:
			files[p2][0] = spaces[p1][0]
			spaces[p1][0] += cur_file_len
			spaces[p1][1] -= cur_file_len
	prev_file = int(cur_file)
	p2 -=1 

files.sort()
# print('final files', files)

checksum = 0
for idx, cur_file_len, cur_file in files:
	for i in range(cur_file_len):
		checksum += (idx +i) * int(cur_file)

print('checksum', checksum)