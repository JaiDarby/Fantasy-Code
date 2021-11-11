from espn_api.football import League
import csv
import pandas as pd
import xlsxwriter

class Player:
	def __init__(self, position, name, projected, score):
		self.position = position
		self.name = name
		self.projected = projected
		self.score = score

league = League(league_id=82131950, year = 2020)

MyTeam = league.teams[1]

BoxScores = league.box_scores(12)

Players = BoxScores[0].away_lineup

e1 = Player("x", "x", 13, 0)
e2 = Player("x", "x", 20, 0)
e3 = Player("x", "x", 23, 0)
e4 = Player("x", "x", 14, 0)
e5 = Player("x", "x", 14, 0)
e6 = Player("x", "x", 10, 0)
e7 = Player("x", "x", 10, 0)
e8 = Player("x", "x", 0, 0)
e9 = Player("x", "x", 9, 0)
e10 = Player("x", "x", 22, 0)
e11 = Player("x", "x", 10, 0)
e12 = Player("x", "x", 7, 0)
e13 = Player("x", "x", 11, 0)
e14 = Player("x", "x", 12, 0)
e15 = Player("x", "x", 14, 0)
e16 = Player("x", "x", 0, 0)
e17 = Player('x', 'x', 69, 420)

Watchlist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17]

PoisitonList = []
NameList = []
ProjList = []
ScoreList = []

Counter=0
for player in Players:
	Watchlist[Counter].position = Players[Counter].position
	Watchlist[Counter].name = Players[Counter].name
	Watchlist[Counter].projected = float(Players[Counter].projected_points)
	Watchlist[Counter].score = float(Players[Counter].points)
	Counter+=1
	
QBList = []
RBList = []
WRList = []
TEList = []
KList = []
DList = []

x = 0

while x < 17:
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

x = 0

for start in Starters:
	PoisitonList.append(Starters[x].position)
	NameList.append(Starters[x].name)
	ProjList.append(Starters[x].projected)
	ScoreList.append(Starters[x].score)
	x+=1

data = pd.DataFrame({'Position': PoisitonList, 'Name': NameList, 'Projected' : ProjList, 'Score' : ScoreList })

datatoexcel = pd.ExcelWriter("PlayerStats.xlsx", engine = 'xlsxwriter')

data.to_excel(datatoexcel, sheet_name= 'Sheet1')

datatoexcel.save()

	
'''
with open('test.csv', 'w', newline='') as csvfile:
	
	fieldnames = ['Player']
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
	
	for player in Players:
		writer.writerow({'Player' : player})

with open('test.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	
	for line in csv_reader:
		print(line)
'''