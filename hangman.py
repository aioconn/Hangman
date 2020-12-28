# Write your code here
import random

tries = 8
my_list = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')
word = random.choice(my_list)
hidden_word = list('-' * len(word))
used_letters = []


def menu():
    print('')
    my_action = input('Type "play" to play the game, "exit" to quit: ')
    if my_action == 'play':
        play()
    elif my_action == 'exit':
        pass
    else:
        menu()


def play():
    global tries
    while tries > 0:
        print('')
        print(''.join(hidden_word))
        guess = input('Input a letter: ')
        if hidden_word == list(word):
            print(f'You guessed the word {word}!')
            print('You survived!')
            break
        if len(guess) != 1 and guess != 0:
            print('You should input a single letter')
            continue
        elif guess != guess.lower() or guess.isalpha() is False:
            print('Please enter a lowercase English letter')
            continue
        elif guess in used_letters:
            print("You've already guessed this letter")
            continue
        elif guess in word:
            action = [i for i in range(len(word)) if word.startswith(guess, i)]
            for i in action:
                hidden_word[i] = guess
            used_letters.append(guess)
        else:
            print("That letter doesn't appear in the word")
            used_letters.append(guess)
            tries -= 1
            if tries == 0:
                print('You lost!')


menu()