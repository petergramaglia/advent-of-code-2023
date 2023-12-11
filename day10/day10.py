# -----------------------------------------------------
# Part 1
# -----------------------------------------------------

def recurse(board, curr_positions, curr_num_steps):
	print("recursing")
	print(board)
	print(curr_positions)
	print(curr_num_steps)
	if len(curr_positions) > 1 and curr_positions[0] == curr_positions[1]: 
		return curr_num_steps
	next_curr_positions = []
	print("next_curr_positions:", next_curr_positions)
	for pos in curr_positions:
		i = pos[0]
		j = pos[1]
		print(board[i][j+1])
		print(board[i][j+1] == "-")
		if j+1 < len(board[0]) and (board[i][j+1] == "7" or board[i][j+1] == "J" or board[i][j+1] == "-"):
			print("a")
			next_curr_positions.append([i, j+1])
		if j-1 < len(board[0]) and (board[i][j-1] == "F" or board[i][j-1] == "L" or board[i][j-1] == "-"):
			print("b")
			next_curr_positions.append([i, j-1])
		if i+1 < len(board) and (board[i+1][j] == "J" or board[i+1][j] == "L" or board[i+1][j] == "|"):
			print("c")
			next_curr_positions.append([i+1, j])
		if i-1 < len(board) and (board[i-1][j] == "F" or board[i-1][j] == "7" or board[i-1][j] == "|"):
			print("d")
			next_curr_positions.append([i-1, j])
		board[i][j] = "."

	if len(next_curr_positions) < 2:
		return curr_num_steps
	return recurse(board, next_curr_positions, curr_num_steps+1)

f = open("day10_input_example.txt")
f = open("day10_input_example_extra.txt")
# f = open("day10_input.txt")

text = f.read()
lines = text.split("\n")

arr = []
for line in lines:
	curr_line = []
	for l in line:
		curr_line.append(l)
	arr.append(curr_line)

s_index = []
for i in range(0, len(arr)):
	for j in range(0, len(arr[i])):
		# print(arr[i][j])
		if arr[i][j] == "S":
			s_index = [i, j]

res = recurse(arr, [s_index], 0)


print("P1 res:", res)

# -----------------------------------------------------
# Part 2
# -----------------------------------------------------

# f = open("day9_input_example.txt")
# f = open("day9_input.txt")

# text = f.read()
# lines = text.split("\n")



# print("P2 res:", res)