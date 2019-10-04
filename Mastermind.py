import random

# Maximum number of guesses:

max_guess = 10


# Colors to choose from:

colors = ['blue', 'red', 'yellow', 'green', 'purple', 'pink', 'orange', 'brown']

# Defining the function for the Code Maker(computer) to generate the color code:

def code_maker(colors):
    winning_combo = []
    nr_colors = 4
    while nr_colors > 0:
        x = random.choice(colors)
        nr_colors = nr_colors - 1
        winning_combo.append(x)
    return winning_combo


# Defining the function for the Code Guesser to guess the color code

def code_guesser(colors):
    choice = []
    nr_colors = 4
    while nr_colors > 0:
        try:
            x = input('Type a color: blue, red, yellow, green, purple, pink, orange or brown. Your choice: ')
        except:
            print('Input error')
        if x == 'blue' or x == 'red' or x == 'yellow' or x == 'green' or x == 'purple' or x == 'pink' or x == 'orange' or x == 'brown':
            nr_colors = nr_colors - 1
            choice.append(x)
        else:
            print('Ooops... please choose either blue, red, yellow, green, purple, pink, orange or brown')
            continue
    return choice



def gameplay():
    guess = code_guesser(colors)

    winning_list = []
    found = []
    found2 = []


    for i in range(len(guess)):

        if guess[i] == start_game[i]:
            found.append(guess[i])
            print('black')
            winning_list.append('black')

            if guess[i] in start_game and guess[i] not in found:
                print('white')

        elif guess[i] in start_game and guess[i] not in found2 and guess[i] not in found:
            found2.append(guess[i])
            print('white')

    if winning_list == ['black', 'black', 'black', 'black']:
        return 1


    else:
        return 0



start_game = code_maker(colors)
print('Welcome to Mastermind!\n\nYou have 10 rounds to guess the color code that consists of 4 colors. Colors to choose from: blue, red, yellow, green, purple, pink, orange, brown. Please note that the colors can repeat.\nAfter each round, you will receive a hint (order does not matter):\n\n   -black- means that a color is correct and in the right place\n   -white- means that a color is correct, but in the wrong place\n\nGood luck!:)')

#print(start_game)

turn = 1


for i in range(max_guess):
    print('\nTurn:',turn)

    G = gameplay()
    if G == 1:
        print('Congratulations!!! You guessed the code! :)')
        break
    elif G == 0:
        print('Not quite..')
    turn = turn + 1



print('\nThe right code was:',start_game)
print('\nThanks for playing Mastermind! :)')



