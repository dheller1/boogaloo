class Actor:
    """ Base class for all kinds of actors in a game, which are the game itself and the players, but there could also
    be additional actors such as NPCs etc.
    Actors are used to define visibility- and ownership concepts.
    They are usually also the top-level objects of the game state tree, because all entities are owned by (associated
    with) some kind of actor. """
    def __init__(self, name):
        self.name = name
