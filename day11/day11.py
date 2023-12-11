# -----------------------------------------------------
# Part 1
# -----------------------------------------------------
f = open("day11_example.txt")
f = open("day11_input.txt")

text = f.read()
lines = text.split("\n")

expanded = []

for i in range(0, len(lines)):
	if lines[i].count("#") == 0:
		expanded.append(lines[i])
	expanded.append(lines[i])

expanded_2 = []

for j in range(0, len(expanded[0])):
	expand = True
	col = []
	for i in range(0, len(expanded)):
		if expanded[i][j] == "#":
			expand = False
		col.append(expanded[i][j])
	if expand:	
		expanded_2.append(col)
	expanded_2.append(col)

hashes = []
for i in range(0, len(expanded_2)):
	for j in range(0, len(expanded_2[0])):
		if expanded_2[i][j] == "#":
			hashes.append([i, j])

res = 0
for i in range(0, len(hashes)):
	for j in range(i+1, len(hashes)):
		res += abs(hashes[i][0] - hashes[j][0]) + abs(hashes[i][1] - hashes[j][1])

print("P1 res:", res)

# -----------------------------------------------------
# Part 2
# -----------------------------------------------------
f = open("day11_example.txt")
f = open("day11_input.txt")

multiply = 1000000

text = f.read()
lines = text.split("\n")

row_expands = set()
col_expands = set()

for i in range(0, len(lines)):
	if lines[i].count("#") == 0:
		row_expands.add(i)

for j in range(0, len(lines[0])):
	expand = True
	for i in range(0, len(lines)):
		if lines[i][j] == "#":
			expand = False
	if expand:	
		col_expands.add(j)

hashes = []
for i in range(0, len(lines)):
	for j in range(0, len(lines[0])):
		if lines[i][j] == "#":
			hashes.append([i, j])

res = 0
for i in range(0, len(hashes)):
	for j in range(i+1, len(hashes)):
		for a in range(min(hashes[i][0], hashes[j][0]), max(hashes[i][0], hashes[j][0])):
			if a in row_expands:
				res += multiply
			else:
				res += 1

		for a in range(min(hashes[i][1], hashes[j][1]), max(hashes[i][1], hashes[j][1])):
			if a in col_expands:
				res += multiply
			else:
				res += 1

print("P2 res:", res)

















