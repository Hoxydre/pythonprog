import os
import sys

class Ant:
	"""
	Fourmi :
	x : Position en x
	y : Position en y
	orientation : Orientation (0 pour Droite, 1 pour Haut, 2 pour Gauche et 3 pour Bas)
	"""
	def __init__(self, x=0, y=0):
		super(Ant, self).__init__()
		self.x = x
		self.y = y
		self.orientation = int(0)
		


class Compartment:
	"""
	Case de l'échequier de Langton
	x : Position en x
	y : Position en y
	polarity : Couleur de la case (1 pour Blanche et -1 pour Noire)
	"""
	def __init__(self, x, y, polarity = 1):
		super(Compartment, self).__init__()
		self.x = x
		self.y = y
		self.polarity = polarity



def move(ant, case):
	tempx = int(ant.x)
	tempy = int(ant.y)
		
	case[tempx][tempy].polarity *= -1

	if case[tempx][tempy].polarity == -1:
		if ant.orientation == 0:
			ant.y = ant.y + 1
			ant.orientation = (ant.orientation-1) % 4
			pass
		elif ant.orientation == 1:
			ant.x = ant.x + 1
			ant.orientation = (ant.orientation-1) % 4
			pass
		elif ant.orientation == 2:
			ant.y = ant.y - 1
			ant.orientation = (ant.orientation-1) % 4
			pass
		else:
			ant.x = ant.x - 1
			ant.orientation = (ant.orientation-1) % 4
			pass
		pass

	else:
		if ant.orientation == 0:
			ant.y = ant.y - 1
			ant.orientation = (ant.orientation+1) % 4
			pass
		elif ant.orientation == 1:
			ant.x = ant.x - 1
			ant.orientation = (ant.orientation+1) % 4
			pass
		elif ant.orientation == 2:
			ant.y = ant.y + 1
			ant.orientation = (ant.orientation+1) % 4
			pass
		else:
			ant.x = ant.x + 1
			ant.orientation = (ant.orientation+1) % 4
			pass
		pass
	pass



def display(ant, case, l):
	for y in range(0, l):
		for z in range(0, l):
			if y == ant.y and z == ant.x:
				print("⬮", end = "")
				pass
			elif case[z][y].polarity == 1:
				print("▯", end = "")
				pass
			elif case[z][y].polarity == -1:
				print("▮", end = "")
				pass
			pass
		print("")
		pass
	print("\n")
	pass



def enlarge(ant, case, l):
	if ant.x >= l or ant.y >=l or ant.x < 0 or ant.y < 0:
		for u in range(l):
			case[u].insert(0, Compartment(u, 0))
			case[u].append(Compartment(u, l))
			pass

		case.insert(0, [None]*(l+2))
		case.append([None]*(l+2))
		for u in range(0, l+2):
			case[l+1][u] = Compartment(l+1, u) 
			case[0][u] = Compartment(0, u)
			pass

		for u in range(1,l+1):
			for v in range(1,l+1):
				case[u][v].x += 1
				case[u][v].y += 1
				pass
			pass
		ant.x += 1
		ant.y += 1
		l += 2
		pass
		

def langton(size, nbMove, ant):

	case = []

	for t in range(size):
		case.append([None]*(size))
		pass


	for a in range(size):
		for b in range(size):
			case[a][b] = Compartment(a, b)
			pass
		pass

	ant.x = size//2
	ant.y = size//2 


	for x in range(nbMove):
		l = len(case)
		enlarge(ant, case, l)
		print(x)
		print("\n")
		display(ant, case, l)
		move(ant,case)
		pass
	pass



size = int(sys.stdin.readline())

if size % 2 == 0:
	size += 1
	pass

nbMove = int(sys.stdin.readline())

myAnt = Ant(0, 0)

langton(size, nbMove, myAnt)

os.system("pause")
