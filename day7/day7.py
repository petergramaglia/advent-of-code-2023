# f = open("day7_input_example.txt")
f = open("day7_input.txt")

text = f.read()
lines = text.split("\n")

order = {'A':13, 'K':12, 'Q':10, 'J':9, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0}


FIVE_PAIR = 60000000000
FOUR_PAIR = 50000000000
FULL_HOUSE = 40000000000
THREE_KIND = 30000000000
TWO_PAIR = 20000000000
ONE_PAIR = 10000000000
HIGH_CARD = 0

scores = {}
bets = {}
hands = []

for line in lines:
	s = line.split()
	hand = s[0]
	bid = s[1]
	# print("hand:", hand)

	verdict = 0
	counts = []
	for i in range(0, len(hand)):
		counts.append(hand.count(hand[i]))
		verdict += 100**((4-i)) * order[hand[i]]

	
	if 5 in counts:
		verdict += FIVE_PAIR
	elif 4 in counts:
		verdict += FOUR_PAIR
	elif 3 in counts and 2 in counts:
		verdict += FULL_HOUSE
	elif 3 in counts:
		verdict += THREE_KIND
	elif counts.count(2) == 4:
		verdict += TWO_PAIR
	elif 2 in counts:
		verdict += ONE_PAIR
	else:
		verdict += HIGH_CARD

	# print(verdict)

	scores[hand] = verdict
	bets[hand] = int(bid)
	hands.append(hand)

hands = sorted(hands, key=lambda x: scores[x])

res = 0
for i in range(0, len(hands)):
	res += (i+1) * bets[hands[i]]

print("part 1 res:", res)


# ----------------------------------------------------------------------------------------------------


# f = open("day7_input_example.txt")
f = open("day7_input.txt")

text = f.read()
lines = text.split("\n")

order = {'A':13, 'K':12, 'Q':10, 'J':0, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}


FIVE_PAIR = 60000000000
FOUR_PAIR = 50000000000
FULL_HOUSE = 40000000000
THREE_KIND = 30000000000
TWO_PAIR = 20000000000
ONE_PAIR = 10000000000
HIGH_CARD = 0

scores = {}
bets = {}
hands = []

for line in lines:
	s = line.split()
	hand = s[0]
	bid = s[1]
	print("hand:", hand)

	verdict = 0
	counts = []
	for i in range(0, len(hand)):
		counts.append(hand.count(hand[i]))
		verdict += 100**((4-i)) * order[hand[i]]

	
	if 5 in counts or (4 in counts and 'J' in hand) or (3 in counts and hand.count('J') == 2) or (2 in counts and hand.count('J') == 3) or (hand.count('J') == 4):
		verdict += FIVE_PAIR
	elif 4 in counts or (3 in counts and 'J' in hand) or (counts.count(2) == 4 and hand.count('J') == 2) or (hand.count('J') == 3):
		verdict += FOUR_PAIR
	elif (3 in counts and 2 in counts) or (counts.count(2) == 4 and 'J' in hand):
		verdict += FULL_HOUSE
	elif 3 in counts or (2 in counts and 'J' in hand):
		verdict += THREE_KIND
	elif counts.count(2) == 4:
		verdict += TWO_PAIR
	elif 2 in counts or 'J' in hand:
		verdict += ONE_PAIR
	else:
		verdict += HIGH_CARD

	print(verdict)

	scores[hand] = verdict
	bets[hand] = int(bid)
	hands.append(hand)

hands = sorted(hands, key=lambda x: scores[x])

res = 0
for i in range(0, len(hands)):
	res += (i+1) * bets[hands[i]]

print("part 2 res:", res)