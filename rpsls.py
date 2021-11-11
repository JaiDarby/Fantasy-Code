import random

rpsls = ['rock', 'paper', 'scissors', 'lizard', 'spock']
x = random.randint(0,4)
Computer = rpsls[x]
'''
Rock crushes Scissors
Paper covers Rock
Scissors cut Paper

Lizard poisons Spock
Scissors decapitate Lizard
Rock crushes Lizard
Lizard eats Paper

Spock vaporizes Rock
Spock smashes Scissors
Paper disproves Spock

'''

'''
elif Computer == '':
		print('')
		print('')
'''

Player = input('What do you choose? (rock, paper, scissors, lizard, spock): ')
if Player.lower() != rpsls[0] and Player.lower() != rpsls[1] and Player.lower() != rpsls[2] and Player.lower() != rpsls[3] and Player.lower() != rpsls[4]:
	print ('that isnt an option')
else:
	print(Computer)
	if Player.lower() == 'scissors':
		if Computer == 'scissors':
			print ('Tie')
		elif Computer == 'paper':
			print ('You Win!')
			print ('Scissors cut Paper')
		elif Computer == 'lizard':
			print ('You win!')
			print ('Scissors decapitates Lizard')
		elif Computer == 'spock':
			print('You lose!')
			print('Spock smashes Scissors')
		elif Computer == '':
				print('You lose!')
				print('Rock crushes Scissors')

	elif Player.lower() == 'rock':
		if Computer == 'rock':
			print ('Tie')
		elif Computer == 'scissors':
			print ('You Win!')
			print ('Rock crushes Scissors')
		elif Computer == 'lizard':
			print ('You win!')
			print ('Rock crushes Lizard')
		elif Computer == 'paper':
			print('You lose!')
			print('Paper covers Rock')
		elif Computer == 'spock':
				print('You lose!')
				print('Spock vaporizes Rock')

	elif Player.lower() == 'paper':
		if Computer == 'paper':
			print ('Tie')
		elif Computer == 'rock':
			print ('You Win!')
			print ('Paper covers Rock')
		elif Computer == 'spock':
			print ('You win!')
			print ('Paper disproves Spock')
		elif Computer == 'scissors':
			print('You lose!')
			print('Scissors cut Paper')
		elif Computer == 'lizard':
				print('You lose!')
				print('Lizard eats Paper')

	elif Player.lower() == 'lizard':
		if Computer == 'lizard':
			print ('Tie')
		elif Computer == 'paper':
			print ('You Win!')
			print ('Lizard eats Paper')
		elif Computer == 'spock':
			print ('You win!')
			print ('Lizard poisons Spock')
		elif Computer == 'scissors':
			print('You lose!')
			print('Scissors decapitate Lizard')
		elif Computer == 'rock':
			print('You lose!')
			print('Rock crushes Lizard')
			

	elif Player.lower() == 'spock':
		if Computer == 'spock':
			print ('Tie')
		elif Computer == 'rock':
			print ('You Win!')
			print ('Spock vaporizes Rock')
		elif Computer == 'scissors':
			print ('You win!')
			print ('Spock smashes Scissors')
		elif Computer == 'paper':
			print('You lose!')
			print('Paper disproves Spock')
		elif Computer == 'lizard':
				print('You lose!')
				print('Lizard poisons Spock')