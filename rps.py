import random

def userGuess(uGuess):
    if uGuess == 'r':
        print('User selects rock')
        return 'ur'
    elif uGuess == 'p':
        print('User selects paper')
        return 'up'
    else:
        print('User selects scissors')
        return 'us'

def computerGuess(cGuess):
    if cGuess == 1:
        print('Computer selects rock')
        return 'cr'
    elif cGuess == 2:
        print('Computer selects paper')
        return 'cp'
    else:
        print('Computer selects scissors')
        return 'cs'

def whowins(x,y):
    if (x == 'ur' and y == 'cs') or (x == 'up' and y == 'cr') or (x == 'us' and y == 'cp'):
        return 'User wins!'
    if (x == 'us' and y == 'cr') or (x == 'ur' and y == 'cp') or (x == 'up' and y == 'cs'):
        return 'Computer wins!'
    if (x == 'ur' and y == 'cr') or (x == 'up' and y == 'cp') or (x == 'us' and y == 'cs'):
        return "It's a tie!"

def main():
    while True:
        uGuess = input('Please select rock (r), paper (p) or scissors (s): ')
        uGuess = uGuess.lower()
        cGuess = random.randint(1, 3)
        x = userGuess(uGuess)
        y = computerGuess(cGuess)
        print(whowins(x,y))
        pagain = input('Press any key to continue playing...')
        pagain = pagain.lower()
        if pagain == 'n':
            break

main()