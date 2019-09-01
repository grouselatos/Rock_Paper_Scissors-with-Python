#vazw ta modules pou tha xreiastw
import random

#Exw treis epiloges, opote ekxwrw lista
choices = ['rock', 'paper', 'scissors']
#to paixnidi teleiwnei sta tria, opote kapws krataw score
player_points = 0
ai_points = 0

while player_points < 3 and ai_points < 3:
    #paizei o paixths
    player_choice = input('Choose rock, paper or scissors: ')
    #tsekareis an h timh einai sth lista alla oxi me repeated and/or(boolean) alla me while/in
    #h synarthsh lower pianei kai ta kefalaia(wste to paixnidi na mhn einai sensitive
    player_choice = player_choice.lower()
    while player_choice not in choices:
       player_choice = input('Choose rock, paper or scissors: ')

    ai_choice = random.choice(choices)
    print('AI chose', ai_choice)
    #exoume ennia pithana senaria, treis isopalies, treis nikes player h treis nikes pc
    #tis omadopoioume se tria yposynola opou tha einai se morfh if-elif-else
    if (player_choice == 'rock' and ai_choice == 'scissors' or
        player_choice == 'paper' and ai_choice == 'rock' or
        player_choice == 'scissors' and ai_choice == 'paper'):
            player_points = player_points + 1
            print('One round to player.')
    #2o senario
    #o xarakthras \ einai ekei wste na mhn akoiksei string me thn '
    elif player_choice == ai_choice:
        print('it\'s a draw')
    #allo scenario
    else:
        ai_points == ai_points + 1
        print('One round to player.')
    #dinei to score
    print('Score - Player:', player_points, 'AI:', ai_points)
'''edw einai pio kalh h lysh giati exei ftiaksei ton ena gyro tou paixnidiou kai ton evale
se ena while'''
if player_points == 3:
    print('Player wins the game.')
else:
    print('AI wins the game.')
