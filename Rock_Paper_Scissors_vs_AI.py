
import random

choices = ['rock', 'paper', 'scissors']

player_points = 0
ai_points = 0

while player_points < 3 and ai_points < 3:

    player_choice = input('Choose rock, paper or scissors: ')

    player_choice = player_choice.lower()
    while player_choice not in choices:
       player_choice = input('Choose rock, paper or scissors: ')

    ai_choice = random.choice(choices)
    print('AI chose', ai_choice)

    if (player_choice == 'rock' and ai_choice == 'scissors' or
        player_choice == 'paper' and ai_choice == 'rock' or
        player_choice == 'scissors' and ai_choice == 'paper'):
            player_points = player_points + 1
            print('One round to player.')

    elif player_choice == ai_choice:
        print('it\'s a draw')

    else:
        ai_points == ai_points + 1
        print('One round to player.')

    print('Score - Player:', player_points, 'AI:', ai_points)

if player_points == 3:
    print('Player wins the game.')
else:
    print('AI wins the game.')
