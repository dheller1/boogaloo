from boogaloo.entities.visibility import Visibility


class GameEntity:
    """ Abstract base class for all entities comprised in the state tree. """
    def __init__(self):
        self.visibility = Visibility.All
