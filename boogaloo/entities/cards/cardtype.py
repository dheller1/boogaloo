from boogaloo.entities import GameEntity


class CardType(GameEntity):
    """ A CardType is an abstract definition of multiple cards which belong together. Often they have the same flipside
    are initially shuffled into the same stacks, but are then distributed among the game and the players.
    Collections of cards, which are concrete containers with specific meanings in the game (e.g. a player hand or
    a draw pile) usually specify which types of cards they can contain.
    Concrete cards (with their front-side and specific functionality) normally also specify which CardType they are
    associated with.
    """
    def __init__(self):
        super().__init__()