# -----------------------------------------------------
# Part 1
# -----------------------------------------------------

f = open("day9_input_example.txt")
f = open("day9_input.txt")

text = f.read()
lines = text.split("\n")

res = 0
for line in lines:
	nums = [[int(x) for x in line.split()]]

	while nums[-1].count(0) != len(nums[-1]):
		new_line = []
		for i in range(1, len(nums[-1])):
			new_line.append(nums[-1][i] - nums[-1][i-1])
		nums.append(new_line)

	adder = 0
	for i in range(len(nums)-1, -1, -1):
		adder += nums[i][-1]
	res += adder

print("P1 res:", res)

# -----------------------------------------------------
# Part 2
# -----------------------------------------------------

f = open("day9_input_example.txt")
f = open("day9_input.txt")

text = f.read()
lines = text.split("\n")

res = 0
for line in lines:
	nums = [[int(x) for x in line.split()]]

	while nums[-1].count(0) != len(nums[-1]):
		new_line = []
		for i in range(1, len(nums[-1])):
			new_line.append(nums[-1][i] - nums[-1][i-1])
		nums.append(new_line)

	adder = 0
	for i in range(len(nums)-1, -1, -1):
		adder = nums[i][0] - adder
	res += adder

print("P2 res:", res)
