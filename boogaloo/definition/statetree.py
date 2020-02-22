from boogaloo.core.tree.node import Node
from boogaloo.core.tree.tree import Tree


class StateTreeDefinition(Tree):
    """ Definition of the entities and their relations in the ruleset of a game.
    The tree definition initializes itself with some fixed nodes which appear in all definitions, most notably
    the root node and, below that, the Global and the Players nodes."""
    def __init__(self):
        super().__init__(StateTreeRootNode())

    def add_global(self, name, entity):
        self.root.globals.add_entity(name, entity)

    def add_per_player(self, name, entity):
        self.root.per_player.add_entity(name, entity)


class StateTreeRootNode(Node):
    """ Special node which is the root of the StateTree. Contains no entities itself.
    It contains two fixed children, the Globals node and the Players node.
    Usually, all nodes will be a child of either one of them: Globals if they are unique in the game,
    Players if each player should receive an instance of the entity.
    Globals and Players should always remain the first and second nodes in the list of children. """
    def __init__(self):
        super().__init__('Root', entity=None)
        self.globals = Node('Globals')
        self.per_player = Node('Per Player')
        self.add_node(self.globals)
        self.add_node(self.per_player)
