from boogaloo.core.tree.tree import Tree


class SessionTree(Tree):
    """ Tree representing the current state of a concrete game session and all its entities.
    The tree initializes itself with some fixed nodes, most notably the root node and, below that,
    the Global and the Players nodes."""
    def __init__(self):
        super().__init__()

    def add_global(self, name, entity):
        self.root.globals.add_entity(name, entity)

    def add_per_player(self, name, entity):
        self.root.per_player.add_entity(name, entity)
