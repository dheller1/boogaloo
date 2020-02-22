from boogaloo.core.tree.node import Node
from boogaloo.core.tree.tree import Tree


class SessionTree(Tree):
    """ Tree representing the current state of a concrete game session and all its entities.
    The tree initializes itself with some fixed nodes, most notably the root node and, below that,
    the Global and the Players nodes."""
    def __init__(self, players):
        super().__init__(SessionTreeRootNode(players))


class SessionTreeRootNode(Node):
    """ Special node which is the root of the SessionTree. Contains no entities itself.
    It contains some fixed children: The Globals node, and one node for each player.
    Usually, all nodes will be a child of one of these. """
    def __init__(self, players):
        super().__init__('Root', entity=None)
        self.globals = Node('Globals')
        self.player_nodes = { p: Node(p.name) for p in players }
        self.add_node(self.globals)
        for pn in self.player_nodes.values():
            self.add_node(pn)
