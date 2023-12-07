f = open("day4_input.txt")
text = f.read()
lines = text.split("\n")

res = 0

for line in lines:
	card_num_cards = line.split(":")
	cards = card_num_cards[1].split("|")
	winning_cards = cards[0].split()
	for i in range(0, len(winning_cards)):
		winning_cards[i] = winning_cards[i].strip()

	my_cards = cards[1].split()
	for i in range(0, len(my_cards)):
		my_cards[i] = my_cards[i].strip()

	points = 0
	for my_card in my_cards:
		if my_card in winning_cards:
			if points == 0:
				points = 1
			else:
				points = points * 2
	res += points

print("part 1 result:", res)

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

f = open("day4_input.txt")
text = f.read()
lines = text.split("\n")

counts = {}
for i in range(0, len(lines)):
	counts[str(i+1)] = 1

for line in lines:
	card_num_cards = line.split(":")
	card_num = card_num_cards[0].split()[1]

	cards = card_num_cards[1].split("|")

	winning_nums = cards[0].split()
	for i in range(0, len(winning_nums)):
		winning_nums[i] = winning_nums[i].strip()

	my_nums = cards[1].split()
	for i in range(0, len(my_nums)):
		my_nums[i] = my_nums[i].strip()

	my_winning_nums = 0
	for my_num in my_nums:
		if my_num in winning_nums:
			my_winning_nums += 1


	for i in range(int(card_num) + 1, int(card_num) + my_winning_nums+1):
		if i > len(lines):
			break
		# print("card num:", card_num)
		# print("i:", i)
		# print(counts)
		counts[str(i)] += counts[card_num]


res = 0
for count in counts:
	res += counts[count]
print(counts)
print("part 2 result:", res)







