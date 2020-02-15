from boogaloo.core.visibility import Visibility


class EntityDefinition:
    """ Abstract base class for all abstract entity definitions comprised in the definition tree. """
    def __init__(self):
        self.visibility = Visibility.All
