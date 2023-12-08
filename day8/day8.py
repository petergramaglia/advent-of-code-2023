# f = open("day8_input_example.txt")
# f = open("day8_input_example_2.txt")

f = open("day8_input.txt")

text = f.read()
lines = text.split("\n")

instr = lines[0]

graph = {}
lines = lines[2:]
left_right = []
lines.sort()

curr_el = ""
last_el = ""

for i in range(0, len(lines)):
	arr = lines[i].split()
	graph[arr[0]] = i
	left = arr[2][1] + arr[2][2] + arr[2][3]
	right = arr[3][0] + arr[3][1] + arr[3][2]
	left_right.append([left, right])

	if i == 0: 
		curr_el = arr[0]
	elif i == len(lines)-1: 
		last_el = arr[0]

# print(left_right)

steps = 0
instr_el = 0
while curr_el != last_el:
	# print("curr el:", curr_el)
	steps += 1
	next_instr = instr[instr_el]
	if next_instr == "R":
		curr_el = left_right[graph[curr_el]][1]
	elif next_instr == "L":
		curr_el = left_right[graph[curr_el]][0]

	instr_el += 1
	if instr_el == len(instr):
		instr_el = 0

print("part 1 res:", steps)

# ---------------------------------------------------------
# f = open("day8_input_example_3.txt")
f = open("day8_input.txt")

text = f.read()
lines = text.split("\n")

instr = lines[0]

graph = {}
lines = lines[2:]
left_right = []
lines.sort()

curr_el = []

for i in range(0, len(lines)):
	arr = lines[i].split()
	graph[arr[0]] = i
	left = arr[2][1] + arr[2][2] + arr[2][3]
	right = arr[3][0] + arr[3][1] + arr[3][2]
	left_right.append([left, right])

	if arr[0][2] == "A": 
		curr_el.append(arr[0])

steps = 0
instr_el = 0

first_z = [-1, -1, -1, -1, -1, -1]

while True:
	for i in range(0, len(curr_el)):
		if curr_el[i][2] == "Z" and first_z[i] == -1:
			first_z[i] = steps

	if first_z.count(-1) == 0: 
		print("breaking")
		break 
			
	steps += 1
	next_curr_el = []
	next_instr = instr[instr_el]
	for c in curr_el:
		if next_instr == "R":
			next_curr_el.append(left_right[graph[c]][1])
		elif next_instr == "L":
			next_curr_el.append(left_right[graph[c]][0])

	instr_el += 1
	if instr_el == len(instr):
		instr_el = 0

	curr_el = next_curr_el



print("part 2 first time each element gets a word ending in Z:", first_z)

# Then, use internet Least Common Multiple calculator to find the LCM: 14265111103729
# I would have used Python's math.lcm() function but my Python version wasn't high enough
# and I didn't want to figure out import issues.



















