import random

choices = ['rock', 'paper', 'scissors']
actions = {'paperrock': 'covers', 'rockscissors': 'smashes', 'scissorspaper': 'cuts'}
scores = [0, 0]
end = [['Your', 'YOU'], ['Computer', 'COMPUTER']]
while scores[0] < 10 and scores[1] < 10:
    user_choice = input('Enter a choice(rock, paper, scissors): ')
    while user_choice.lower() not in choices:
        if user_choice == 'quitgame':
            print('FINISH')
            exit()
        print('You chose a rong choice, please try again')
        user_choice = input('Enter a choice(rock, paper, scissors): ')
    computer_choice = random.choice(choices)
    print(f'You chose {user_choice}, computer chose {computer_choice}.')
    if not (choices.index(user_choice) - choices.index(computer_choice)):
        print(f"Both players selected {user_choice}. It's a tie!")
    elif (choices.index(user_choice) - choices.index(computer_choice)) % 3 - 1:
        scores[1] += 1
        print(f'{computer_choice} {actions[computer_choice + user_choice]} {user_choice}! computer scored 1 point, your score is {scores[0]}, computer score is {scores[1]}'.capitalize())
    else:
        scores[0] += 1
        print(f'{user_choice} {actions[user_choice + computer_choice]} {computer_choice}! you scored 1 point, your score is {scores[0]}, computer score is {scores[1]}'.capitalize())
print(f'=====================================\n{end[scores.index(max(scores))][0]} score reach 10. {end[scores.index(max(scores))][1]} WIN\n=====================================')
