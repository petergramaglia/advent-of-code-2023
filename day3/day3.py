f = open("day3_input.txt")
text = f.read()
lines = text.split("\n")

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

res = 0

for i in range(0, len(lines)):
	curr_str = ""
	# print(lines[i])
	for j in range(0, len(lines[i])):
		if lines[i][j] in nums:
			curr_str += lines[i][j]
		if curr_str == "":
			continue
		if j+1 == len(lines[0]) or lines[i][j+1] not in nums:
			num_start_index = j + 1 - len(curr_str)
			num_end_index = j + 1 - 1
			count_this_one = False
			for a in range(i-1, i+2):
				for b in range(num_start_index - 1, num_end_index + 2):
					# print(a, b)
					if a >= 0 and a < len(lines) and b >= 0 and b < len(lines[0]) and lines[a][b] not in nums and lines[a][b] != '.':
						count_this_one = True
						break
				if count_this_one:
					break
			if count_this_one:
				res += int(curr_str)
				# print("counting", curr_str)
			# else:
				# print("not counting", curr_str)
			curr_str = ""

print("part 1 answer:", res)


# --------------------------------------------------------------------------

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

res = 0

nums_found = {}

for i in range(0, len(lines)):
	curr_str = ""
	# print(lines[i])
	for j in range(0, len(lines[i])):
		if lines[i][j] in nums:
			curr_str += lines[i][j]
		if curr_str == "":
			continue
		if j+1 == len(lines[0]) or lines[i][j+1] not in nums:
			
			num_start_index = j + 1 - len(curr_str)
			num_end_index = j + 1 - 1
			found_gear = False

			for a in range(i-1, i+2):
				for b in range(num_start_index - 1, num_end_index + 2):
					# print(a, b)
					if a >= 0 and a < len(lines) and b >= 0 and b < len(lines[0]):
						# print("nums found:", nums_found)
						# print("a:", a, "b:", b)
						# print("curr_str:", curr_str)
						if lines[a][b] == '*':
							nums_found[a*1000 + b] = int(curr_str)
							found_gear = True		
							# print(lines[a])					
							lines[a] = lines[a][:b] + 'g' + lines[a][b+1:]
							# print(lines[a])
							break
						elif lines[a][b] == 'g':
							gear_ratio = nums_found[a*1000 + b] * int(curr_str)
							res += gear_ratio
				if found_gear: break

			curr_str = ""

print("part 2 answer:", res)
