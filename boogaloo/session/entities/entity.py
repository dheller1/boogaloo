from boogaloo.core.visibility import Visibility


class Entity:
    """ Abstract base class for all concrete entities comprised in the game state tree. """
    def __init__(self):
        self.visibility = Visibility.All
        self.owner = None
