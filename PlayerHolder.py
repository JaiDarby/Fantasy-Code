import time

class Player:
	def __init__(self, position, name, projected, score):
		self.position = position
		self.name = name
		self.projected = projected
		self.score = score

def bubble_sort(array):
	n = len(array)
	for i in range(n):
		already_sorted = True
		for j in range(n - i - 1):
			if array.projected[j] > array.projected[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				already_sorted = False
		if already_sorted:
			break
	return array


e1 = Player("QB", "Josh Allen", 13, 0)
e2 = Player("RB", "Dalvin Cook", 20, 0)
e3 = Player("RB", "Alvin Kamara", 23, 0)
e4 = Player("WR", "Kenny Golladay", 14, 0)
e5 = Player("WR", "DJ Moore", 14, 0)
e6 = Player("TE", "Hayden Hurst", 10, 0)
e7 = Player("RB", "Chris Carson", 10, 0)
e8 = Player("D/ST", "Steelers", 0, 0)
e9 = Player("K", "Justin Tucker", 9, 0)
e10 = Player("QB", "Matt Ryan", 22, 0)
e11 = Player("TE", "Jared Cook", 10, 0)
e12 = Player("RB", "Cam Akers", 7, 0)
e13 = Player("RB", "Antonio Gibson", 11, 0)
e14 = Player("WR", "DJ Chark Jr.", 12, 0)
e15 = Player("WR", "Tyler Boyd", 14, 0)
e16 = Player("QB", "Dak Prescott", 0, 0)

Watchlist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
QBList = []
RBList = []
WRList = []
TEList = []
KList = []
DList = []

x = 0

while x < 16:
	#QuarterBacks
	if Watchlist[x].position == "QB":
		QBList.append(Watchlist[x])
	#Running Backs
	if Watchlist[x].position == "RB":
		RBList.append(Watchlist[x])
	#Wide Recivers
	if Watchlist[x].position == "WR":
		WRList.append(Watchlist[x])
	#Tight Ends
	if Watchlist[x].position == "TE":
		TEList.append(Watchlist[x])
	#Kicekrs
	if Watchlist[x].position == "K":
		KList.append(Watchlist[x])
	#Defense
	if Watchlist[x].position == "D/ST":
		DList.append(Watchlist[x])	
	
	x += 1

QBList.sort(key = lambda Player:Player.projected, reverse = True)
RBList.sort(key = lambda Player:Player.projected, reverse = True)
TEList.sort(key = lambda Player:Player.projected, reverse = True)
WRList.sort(key = lambda Player:Player.projected, reverse = True)
KList.sort(key = lambda Player:Player.projected, reverse = True)
DList.sort(key = lambda Player:Player.projected, reverse = True)

#Figure Out Starting Linup
Starters = []
#Starting Quarterback
Starters.append(QBList[0])
#Starting Running Backs
Starters.append(RBList[0])
Starters.append(RBList[1])
#Starting Wide Recivers
Starters.append(WRList[0])
Starters.append(WRList[1])
#Starting Tightends
Starters.append(TEList[0])
#Starting Flex
if RBList[2].projected > WRList[2].projected and RBList[2].projected > TEList[1].projected:
	Starters.append(RBList[2])
elif WRList[2].projected > RBList[2].projected and WRList[2].projected > TEList[1].projected:
	Starters.append(WRList[2])
else:
	Starters.append(TEList[1])
#Starting Defense
Starters.append(DList[0])
#Starting Kicker
Starters.append(KList[0])

y=0
for i in Starters:
	print (Starters[y].name)
	y+=1
	
