f = open("day5_input_example.txt")
text = f.read()
lines = text.split("\n")

seeds = lines[0].split()[1:]
# print(seeds)

graphs = ['seed-to-soil',
'soil-to-fertilizer',
'fertilizer-to-water',
'water-to-light',
'light-to-temperature',
'temperature-to-humidity',
'humidity-to-location']


for seed in seeds:
	seed = int(seed)

seeds_set = []
for seed in seeds:
	seeds_set.append([int(seed)])

line_num = 1
seed_set_num = -1

while line_num < len(lines):
	if lines[line_num] == '':
		# print("line_num += 1")
		line_num += 1
		# print("line_num", line_num)

	if lines[line_num].split()[0] in graphs:
		# print("seed_set_num += 1, line_num += 1")
		seed_set_num += 1
		line_num += 1
		# print("line num:", line_num)
		# print("seed_set_num", seed_set_num)
		# print(seeds_set)

	while line_num < len(lines) and lines[line_num] != '':
		map_bound = int(lines[line_num].split()[0])
		low_bound = int(lines[line_num].split()[1])
		high_bound = low_bound + int(lines[line_num].split()[2])

		for i in range(len(seeds_set)):
			if len(seeds_set[i])-1 > seed_set_num:
				continue

			seed = seeds_set[i][seed_set_num]
			if seed >= low_bound and seed < high_bound:
				new_seed = map_bound + (seed - low_bound)
				seeds_set[i].append(new_seed)
		line_num += 1

	for i in range(len(seeds_set)):
		# print("------------")
		# print(seed_set_num)
		# print(seeds_set[i])
		if len(seeds_set[i]) != seed_set_num+2:
			seeds_set[i].append(seeds_set[i][-1])
	# print(seeds_set)

res = []
for s in seeds_set:
	res.append(s[-1])

print("part 1 result:", min(res))


# ---------------------------------------------------------------------

f = open("day5_input.txt")
text = f.read()
lines = text.split("\n")

seed_ranges = lines[0].split()[1:]
print("seed ranges:", seed_ranges)
seeds = set()
count = 0
for i in range(0, len(seed_ranges), 2):

	for j in range(0, int(seed_ranges[i+1])):
		seeds.add(int(seed_ranges[i]) + j)
		count += 1
		if count % 10000000 == 0:
			print(count)


# print(seeds)

graphs = ['seed-to-soil',
'soil-to-fertilizer',
'fertilizer-to-water',
'water-to-light',
'light-to-temperature',
'temperature-to-humidity',
'humidity-to-location']


for seed in seeds:
	seed = int(seed)

seeds_set = []
for seed in seeds:
	seeds_set.add([int(seed)])

line_num = 1
seed_set_num = -1

while line_num < len(lines):
	if lines[line_num] == '':
		line_num += 1

	if lines[line_num].split()[0] in graphs:
		seed_set_num += 1
		line_num += 1


	while line_num < len(lines) and lines[line_num] != '':
		map_bound = int(lines[line_num].split()[0])
		low_bound = int(lines[line_num].split()[1])
		high_bound = low_bound + int(lines[line_num].split()[2])

		for i in range(len(seeds_set)):
			if len(seeds_set[i])-1 > seed_set_num:
				continue

			seed = seeds_set[i][seed_set_num]
			if seed >= low_bound and seed < high_bound:
				new_seed = map_bound + (seed - low_bound)
				seeds_set[i].append(new_seed)
		line_num += 1

	for i in range(len(seeds_set)):
		if len(seeds_set[i]) != seed_set_num+2:
			seeds_set[i].append(seeds_set[i][-1])
	# print(seeds_set)

res = []
for s in seeds_set:
	res.append(s[-1])

print("part 2 result:", min(res))












	














	




