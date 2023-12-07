f = open("day1_input.txt")
text = f.read()
lines = text.split()
map = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

map2 = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

res = 0

for line in lines:
	first = 0
	last = 0
	for i in range(0, len(line)):
		if line[i] in map:
			first = map[line[i]]
			break
	for j in range(len(line)-1, -1, -1):
		if line[j] in map:
			last = map[line[j]]
			break

	res += 10*first + last

print(res)

# -------------------------------------------------

res2 = 0

for line in lines:
	first = 0
	last = 0
	print("line:", line)
	for i in range(0, len(line)):
		# print("line:", line)

		if line[i] in map:
			if first == 0:
				first = map[line[i]]
			else:
				last = map[line[i]]

		for j in range(i+1, i+7):
			# print("i:", i, "j:", j)
			# if j < len(line): print(line[i:j])
			if j < len(line)+1 and (line[i:j] in map2):
				if first == 0:
					first = map2[line[i:j]]
					break
				else:
					last = map2[line[i:j]]
		
	print("first:", first)
	print("last:", last)
	if last == 0:
		last = first
	res2 += 10*first + last

print(res2)