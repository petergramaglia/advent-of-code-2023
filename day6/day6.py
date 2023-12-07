f = open("day6_input.txt")
text = f.read()
lines = text.split("\n")


times = lines[0].split()[1:]
dists = lines[1].split()[1:]



res = 1
for i in range(0, len(times)):
	dist = int(dists[i])
	time = int(times[i])
	ways_to_win = 0
	for j in range(0, time):
		if (time-j) * j > dist:
			ways_to_win += 1
	res *= ways_to_win
print("part 1 res:",res)

# ------------------------------

times = lines[0].split()[1:]
dists = lines[1].split()[1:]
time = ""
dist = ""
for i in range(0, len(times)):
	time += times[i]
	dist += dists[i]

time_int = int(time)
dist_int = int(dist)




ways_to_win = 0
for j in range(0, time_int):
	if (time_int-j) * j > dist_int:
		ways_to_win += 1

print("part 2 res:",ways_to_win)

