from . import Actor


class Player(Actor):
    def __init__(self, player_id):
        super().__init__(f'Player {player_id + 1}')
