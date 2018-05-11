import math
import itertools
import copy

# Helper Function to return a list of the possible combinations of a list of numbers 
def GetValues(num):
	return sum([map(list, itertools.combinations(num, i)) for i in range(len(num) + 1)], [])[1:]

# Helper Function to turn a list into a string
def stRep(l):
	output = ""
	for x in l:
		output += str(x)
	return output

# Return the shapley value for numPLayers players using the given values v
def ShapleyValue(v,numPlayers):
	players = range(numPlayers)
	values = GetValues(range(numPlayers))
	payoff = {}
	for x in range(len(v)):
		payoff[stRep(values[x])] = v[x]
	comb = list(itertools.permutations(range(numPlayers)))
	scores = {}
	for i in players:
		scores[i] = 0
	#iterate through each possible ordering and calculate marginal values
	for x in comb:
		z = list(x)
		previous = 0
		for y in range(len(z)):
			m = z[0:y+1]
			m.sort()
			scores[z[y]] += (payoff[stRep(m)] - previous)
			previous = payoff[stRep(m)]
	#divide each total marginal value by the number of possible orderings and print out each Shapley Value
	for x in scores:
		scores[x] /= float(len(comb))
		print("Shapley Value for Player " + str(x) + " is: " + str(scores[x]))



#print(ShapleyValue([7,4,6,7,15,9,19],3))
#print(list(itertools.permutations(range(4))))

anotherGame = True
while(anotherGame):
	numPlayers = raw_input('Enter number of players: ')
	coalitions = GetValues(range(int(numPlayers)))
	values = []
	for coalition in coalitions:
		value = raw_input('Enter value for coalition ' + str(coalition) +": ")
		values += [int(value)]
	ShapleyValue(values,int(numPlayers))
	response = raw_input('Type Yes if you want to calculate another game: ')
	if response != "Yes":
		anotherGame = False




