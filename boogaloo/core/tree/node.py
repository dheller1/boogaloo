class Node:
    """ Node in a which may or may not hold entities.
    Nodes without entities are often parents of other nodes which are grouped together.
    Nodes can only ever have a single parent, which is a read-only property. To attach a node
    to a new parent, use `reparent()` or call `add_node()` on the parent node. """
    def __init__(self, name, entity=None):
        self.name = name
        self.entity = entity
        self.children = list()
        self._parent = None
        self.depth = 0

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
        self.depth = self._parent.depth + 1

    def add_node(self, node):
        assert not self.contains(node.name)
        assert node.parent in (None, self)
        node.reparent(self)

    def _add_child(self, child):
        self.children.append(child)

    def _remove_child(self, child):
        self.children.remove(child)

    def add_entity(self, name, entity):
        assert not self.contains(name)
        self.add_node(Node(name, entity))

    def contains(self, name):
        for c in self.children:
            if c.name == name:
                return True
        return False

    def __iter__(self):
        yield self
        for child in self.children:
            for node in child:
                yield node


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
