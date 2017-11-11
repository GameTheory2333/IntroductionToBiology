import random as rnd

#-----------------Parameters modified here-----------------#
# Define the utility matrix here
U = [[[2,-1],[3,0]],[[2,3],[-1,0]]]  # The matrix is 2 by 2 by 2

# Define the game scality here
N = 100  # Initial number of players
P = 0.5  # Initial strategy of players
R = 30   # The rounds played
M = 200  # The number of games played in each round


#-------------------Classes defined here-------------------#
# Class for the each player
class player:
	def __init__(self, idex, p0):
		self._id = idex          # The index of the player, which will be set at the initial
		self._initstrategy = p0  # The player should have an initial strategy, which is same for everyone in base model
		self._strategy = {}      # The player can distinguish each other in the base model so the strategies stored in a dictionary
		self._points = 0         # The initial score of the player is 0

	def index(self):             # Get id of the player
		return self._id

	def strategy(self, idx = -1):
		if idx == -1:                    # Default return the strategy
			return self._strategy
		else:                            # Return the certain strategy
			return self._strategy[idx]

	def add_strategy(self, idx):         # Add a new strategy if it not exists
		self._strategy[idx] = self._initstrategy

	#----------------To be implenmented----------------#
	def modify_strategy(self):
		pass
	#----------------To be implenmented----------------#

	def points(self):
		return self._points

	def add_points(self, u):
		self._points += u

	def playwith(self, adversary):
		if adversary.index() in self.strategy():
			pass
		else:
			self.add_strategy(adversary.index())
		action = rnd.random()
		if action <= self.strategy(adversary.index()):
			return 0                     # 0 means cooperation
		else:
			return 1                     # 1 means betrayal

# Class for the game
class game:
	def __init__(self, n, p0, M):
		self.utility = M                         # The utility matrix for each game
		self._population = n                     # The number of players is a certain number in the base model
		self._players = []                       # Generate the list of players where each has an id and same initial strategy
		for i in range(n):
			self._players.append(player(i, p0))

	def population(self):            # Get the number of the players
		return self._population

	def players(self, idex):         # Visit a player of a certain index
		return self._players[idex]

	def play(self, rounds, m):       # Play the game with a certain rounds and for each rounds there is m times match
		for i in range(rounds):
			for j in range(m):
				id_a = rnd.randint(0, self.population() - 1)  # Player one
				id_b = rnd.randint(0, self.population() - 1)  # Player two
				while id_b == id_a:                           # Player two should be the same as player one
					id_b = rnd.randint(0, self.population() - 1)

				action_a = self.players(id_a).playwith(self.players(id_b)) # The action of player one
				action_b = self.players(id_b).playwith(self.players(id_a)) # The action of player two
				
				self.players(id_a).add_points(self.utility[0][action_a][action_b]) # Update the score of player one
				self.players(id_b).add_points(self.utility[1][action_a][action_b]) # Update the score of player two

				#---------These two claues need modifying(and also maybe their position)---------#
				self.players(id_a).modify_strategy()
				self.players(id_b).modify_strategy()
				#---------These two claues need modifying(and also maybe their position)---------#


#---------------Main program goes from here----------------#
new_game = game(N, P, U)
new_game.play(R, M)
