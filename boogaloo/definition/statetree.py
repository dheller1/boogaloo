from boogaloo.core.tree.tree import Tree


class StateTreeDefinition(Tree):
    """ Definition of the entities and their relations in the ruleset of a game.
    The tree definition initializes itself with some fixed nodes which appear in all definitions, most notably
    the root node and, below that, the Global and the Players nodes."""
    def __init__(self):
        super().__init__()

    def add_global(self, name, entity):
        self.root.globals.add_entity(name, entity)

    def add_per_player(self, name, entity):
        self.root.per_player.add_entity(name, entity)
