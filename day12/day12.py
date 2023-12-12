# -----------------------------------------------------
# Part 1
# -----------------------------------------------------
f = open("day12-0.txt")
f = open("day12-1.txt")
f = open("day12.txt")

text = f.read()
lines = text.split("\n")

def is_valid(line, stats):
	# print(line)
	# print(stats)
	real_stats = []
	curr_damaged = False
	for l in line:
		if l == "#":
			if curr_damaged: 
				real_stats[-1] += 1
			else:
				real_stats.append(1)
				curr_damaged = True
		else:
			curr_damaged = False
	# print(real_stats)
	if real_stats == stats:
		return 1
	else:
		return 0

def rec(line, stats):
	# print("rec line:", line)
	if line.count("?")  == 0:
		return is_valid(line, stats)
	for i in range(0, len(line)):
		if line[i] == "?":
			l1 = line[:i] + "#" + line[i+1:]
			l2 = line[:i] + "." + line[i+1:]
			# print(l1)
			# print(l2)
			return rec(l1, stats) + rec(l2, stats)
res = 0
for row in lines:
	line, arr = row.split()
	arr2 = arr.split(",")
	array = [int(x) for x in arr2]
	# print(is_valid(line, array))
	res += rec(line, array)







print("P1 res:", res)

# -----------------------------------------------------
# Part 2
# -----------------------------------------------------
f = open("day12.txt")
f = open("day12.txt")

multiply = 1000000

text = f.read()
lines = text.split("\n")



# print("P2 res:", res)

















