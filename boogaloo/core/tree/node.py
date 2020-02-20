class Node:
    """ Node in the StateTree which may or may not hold actual game entities.
    Nodes without entities are often parents of other nodes which are grouped together.
    Nodes can only ever have a single parent, which is a read-only property. To attach a node
    to a new parent, use `reparent()` or call `add_node()` on the parent node. """
    def __init__(self, name, entity=None):
        self.name = name
        self.entity = entity
        self._children = list()
        self._parent = None

    def __repr__(self):
        return f'Node({self.name}, Entity={self.entity})'

    @property
    def parent(self):
        return self._parent

    # noinspection PyProtectedMember
    def reparent(self, new_parent):
        if new_parent is self._parent:
            return
        if self._parent is not None:
            self._parent._remove_child(self)

        self._parent = new_parent
        self._parent._add_child(self)

    def add_node(self, node):
        assert not self.contains(node.name)
        assert node.parent in (None, self)
        node.reparent(self)

    def _add_child(self, child):
        self._children.append(child)

    def _remove_child(self, child):
        self._children.remove(child)

    def add_entity(self, name, entity):
        assert not self.contains(name)
        self.add_node(Node(name, entity))

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
        super().__init__('Root', entity=None)
        self.globals = GlobalsNode()
        self.per_player = PlayersNode()
        self.add_node(self.globals)
        self.add_node(self.per_player)


class GlobalsNode(Node):
    """ Special node which contains all entities representing a global game state, i.e. they only exist once
    and not once for each player. """
    def __init__(self):
        super().__init__('Globals', entity=None)


class PlayersNode(Node):
    """ Special node which contains one sub-node for each player in the game. When the game starts, all
    nodes/entities below this node will be instantiated N times, once for each player. """
    def __init__(self):
        super().__init__('Players', entity=None)
