from .node import RootNode


class Tree:
    """ Generic tree data structure which contains a root node and usually a hierarchy of nodes below that. """
    def __init__(self):
        self.root = RootNode(self)

    def __iter__(self):
        return (node for node in self.root)
