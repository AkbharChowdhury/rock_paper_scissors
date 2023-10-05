def outcome():
    lose = 'You lose!'
    win = 'You Win!'
    return {
        'rock': {
            'paper': lose,
            'scissors': win
        },
        'scissors': {
            'rock': lose,
            'paper': win
        }
        ,
        'paper': {
            'scissors': lose,
            'rock': win
        }
    }


def options():
    return {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors'
    }


def play_game():
    from random import choice
    choices = list(options().keys())
    computer = choice(choices)
    player = None
    while player not in options():
        player = input('rock, paper or scissors?: (r,p, s): ').lower()

    def show_results():
        print(f'Computer choose {options().get(computer).capitalize()}')
        print(f'Player choose {options().get(player).capitalize()}')

    if player == computer:
        show_results()
        print('Tie!')
        return
    show_results()
    c = options()
    print(outcome()[c.get(player)][c.get(computer)])
