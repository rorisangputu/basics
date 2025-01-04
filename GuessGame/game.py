srt_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the number: '))
    guess_count += 1
    if(guess == 9):
        print('You Won!')
        break

    if(guess_count == guess_limit): print('You lost')
    
1


