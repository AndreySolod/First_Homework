# n = int(input('Enter the number of command:'))
commands = input().split()
n = len(commands)
import random
class game:
	win = 0
	fail = 0
	draw = 0
	goal = 0
	skip = 0
	score = 0
result = {}
for i in range(n):
	for j in range(i + 1, n):
			if result.get(commands[i]) == None:
				result[commands[i]] = game()
			if result.get(commands[j]) == None:
				result[commands[j]] = game()
			r = random.randint(0,6)
			result[commands[i]].goal += r
			result[commands[j]].goal += 6 - r
			result[commands[i]].skip += 6 - r
			result[commands[j]].skip += r
			if r < 3:
				result[commands[i]].fail += 1
				result[commands[j]].win += 1
				result[commands[j]].score += 3
			elif r == 3:
				result[commands[i]].draw += 1
				result[commands[i]].score += 1
				result[commands[j]].draw += 1
				result[commands[j]].score += 1
			elif r > 3:
				result[commands[i]].win += 1
				result[commands[i]].score += 3
				result[commands[j]].fail += 1
arrscore = []
for value in result.values():
	arrscore.append(value.score)
arrscore = list(set(arrscore))
arrscore.sort()
arrscore.reverse()
for i in arrscore:
	for keys, values in result.items():
		if i == values.score:
			print (keys,'\t', n - 1, '\t', values.win, '\t',
			values.draw, '\t', values.fail, '\t', values.goal, '\t', values.skip, '\t', i)