f = open("day2_input.txt")
text = f.read()
lines = text.split("\n")

# 12 red cubes, 13 green cubes, and 14 blue cubes
RED = 12
GREEN = 13
BLUE = 14

res = 0

for line in lines:
	# print(line)
	els = line.split(":")

	game_num = els[0][4:]
	# print("game num:", game_num)
	runs = els[1].split(";")
	broken = False
	# print("runs:", runs)

	for run in runs:
		# print("run:", run)
		
		colors = run.split(", ")
		# print("colors:", colors)
		for color in colors:
			# print("color:", color)
			num_and_color = color.split()
			if num_and_color[1] == 'red' and int(num_and_color[0]) > RED:
				# print("red broken --------------")
				broken = True
			elif num_and_color[1] == 'green' and int(num_and_color[0]) > GREEN:
				# print("green broken --------------")
				broken = True
			elif num_and_color[1] == 'blue' and int(num_and_color[0]) > BLUE:
				# print("blue broken --------------")
				broken = True

			if broken: break
		if broken: break


	# print("broken:", broken)
	if not broken:
		# print("adding game num:", int(game_num))
		res += int(game_num)
	# print("res:", res)
print(res)



# ----------------------------------------------------------

f = open("day2_input.txt")
text = f.read()
lines = text.split("\n")

res = 0

for line in lines:
	print(line)
	els = line.split(":")

	runs = els[1].split(";")
	print("runs:", runs)

	min_red = 0
	min_green = 0
	min_blue = 0

	for run in runs:
		print("beginnign of run")
		print("run:", run)
		print("min_red:", min_red)
		print("min_green:", min_green)
		print("min_blue:", min_blue)

		
		colors = run.split(", ")
		# print("colors:", colors)
		for color in colors:
			# print("color:", color)
			num_and_color = color.split()
			print(num_and_color)
			if num_and_color[1] == 'red':
				min_red = max(min_red, int(num_and_color[0]))
				print("min_red:", min_red)
			elif num_and_color[1] == 'green':
				min_green = max(min_green, int(num_and_color[0]))
				print("min_green:", min_green)
			elif num_and_color[1] == 'blue':
				min_blue = max(min_blue, int(num_and_color[0]))
				print("min_blue:", min_blue)

	power = min_red * min_green * min_blue
	print("power:", power)
	res += power

print(res)


