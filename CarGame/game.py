start = 'Car started...Ready to go!'
stop = 'Car stopped'
game_help = '''
start - to start the car
stop - to stop the car
quit - to exit game
'''
game_input = ''
while game_input != 'quit':
    game_input = input('> ').lower()
    if(game_input == 'start'): 
        print(start)
    elif(game_input == 'stop'): 
        print(stop)
    elif game_input == 'help': 
        print(game_help) 
    elif game_input not in ['start', 'stop', 'help', 'quit']:
        print('I dont understand. Try again')
    if(game_input == 'quit'):
        print('Quitting game..')
        break
    


