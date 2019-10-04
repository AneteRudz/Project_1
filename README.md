<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of Your Project
Anete Rudzite

Data Analytics, Amsterdam, 10/4/2019

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
For the first project I decided to build the game 'Mastermind'. I remember playing this game in my childhood on an actual board and tought it would be interesting to see how the Python code would look like.

## Rules
1.	Pleayers: Code Maker (computer) and Code Guesser (user)
2.	Computer randomly creates a row of eight colors: blue, red, yellow, green, purple, pink, orange or brown. One color can be used multiple times.
3.	Goal of the game is for the Code Guesser to guess the code with maximum of 10 guesses
4.	Code Guesser selects the first four colors. Code Maker provides feedback with two colors: white and black (order does not matter)
        •	White – one of the four guessed colors is correct, but is in the wrong place
        •	Black – one of the four guessed colors is correct and is in the right place
5.	Repeat with the next row. 
6.	Game ends as soon as the Code Guesser guesses the code or if there are no more guesses left.

## Workflow
 - Import random module.
 - Assign to a variable the number of max guesses (10).
 - Define a function to generate the 'winning combination' that consists of 4 random colors. Colors to choose from: blue, red, yellow, green, purple, pink, orange or brown (colors can repeat).
 - Define a function to guess the four color combination.
     . Ask for the user input until four colors are selected. Create a list with the user's choice.
 - Define a function for the gameplay:
     . Exectue the guess function.
     . Loop through the list with user's color choice. 
         - If the element is in the 'winning combination' and in the correct position - print 'black'. Add each 'black' string to a list called 'winning_list'.
         - If the element is in the 'winning combination' but not in the correct position - print 'white'.
     . Check if the 'winning_list' contains the following: ('black', 'black', 'black', 'black'). If yes, return 1.
 - Start the game by executing the function that generates the 'winning combination'.
 - Create a loop where the game is being played:
     . Indicate the current turn.
     . Execute the gameplay function.
     . Define the winning condition - if all four colors are guessed correcly and the 'winning_list' contains ('black', 'black', 'black', 'black'), game ends. Otherwise user has 10 turns to guess the 'winning combination'.
     . Display the original 'winning combination' at the end of the game.

## Organization
To organize my work I used Trello. This allowed me to plan my tasks and to see how far in the process I am.
The GitHub repository consists of the README file, pseudocode, previous versions of the code (Jupyter notebook files) and the final version of the code (py file).

## Links

[Repository](https://github.com/AneteRudz/Project_1.git)  
[Trello](https://trello.com/b/yuJYrKdo/project-1)
