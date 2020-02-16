class Node:
    """ Node in the StateTree which may or may not hold actual game entities.
    Nodes without entities are often parents of other nodes which are grouped together. """
    def __init__(self, name, parent=None, entity=None):
        self.name = name
        self.entity = entity
        self.parent = parent
        self._children = list()

    def add_node(self, node):
        assert not self.contains(node.name)
        assert node.parent in (None, self)
        node.parent = self
        self._children.append(node)

    def add_entity(self, name, entity):
        assert not self.contains(name)
        self.add_node(Node(name, self, entity))

    def contains(self, name):
        for c in self._children:
            if c.name == name:
                return True
        return False

    def __iter__(self):
        yield self
        for child in self._children:
            for node in child:
                yield node


class RootNode(Node):
    """ Special node which is the root of the StateTree. Contains no entities itself.
    Its parent is the StateTree itself.
    It contains two fixed children, the Globals node and the Players node.
    Usually, all nodes will be a child of either one of them: Globals if they are unique in the game,
    Players if each player should receive an instance of the entity.
    Globals and Players should always remain the first and second nodes in the list of children. """
    def __init__(self, tree):
        super().__init__("Root", tree, entity=None)
        self.globals = GlobalsNode(self)
        self.per_player = PlayersNode(self)
        self._children.append(self.globals)
        self._children.append(self.per_player)


class GlobalsNode(Node):
    """ Special node which contains all entities representing a global game state, i.e. they only exist once
    and not once for each player. """
    def __init__(self, parent):
        super().__init__("Globals", parent, entity=None)


class PlayersNode(Node):
    """ Special node which contains one sub-node for each player in the game. When the game starts, all
    nodes/entities below this node will be instantiated N times, once for each player. """
    def __init__(self, parent):
        super().__init__("Players", parent, entity=None)
