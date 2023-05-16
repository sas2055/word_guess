import random as rdm
name = input('What is your name? ')
print('Good Luck: ', name)
words = ['Python', 'is', 'high', 'level', 'and', 'interpreted', 'Programming', 'langauge']
word = rdm.choice(words)
print('Please guess the characters: ')
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:
        print('User Win')
        print('The correct word is: ', word)
        break
    guess1 = input('Guess another character: ')
    guesses += guess1
    if guess1 not in word:
        turns -= 1
        print('Wrong Guess')
        print('You have ', + turns, 'more guesses ')
        if turns == 0:
            print('User Loose')