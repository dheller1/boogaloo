from boogaloo.core.tree.node import Node
from boogaloo.definition.entities.cards import HandDefinition
from boogaloo.session.actors.gameactor import GameActor
from boogaloo.session.actors.player import Player
from boogaloo.session.sessiontree import SessionTree
from boogaloo.session_factory.builders.handofcardsbuilder import HandOfCardsBuilder

import logging


class Factory:
    Builders = {
        HandDefinition: HandOfCardsBuilder(),
    }

    def __init__(self):
        self._nodedict = {}  # maps definition nodes to the session nodes generated from them

    def build_tree(self, tree_def, num_players):
        players = list(Factory.build_players(num_players))

        tree = SessionTree(players)
        # register pre-built nodes
        self._register(tree_def.root, tree.root)
        self._register(tree_def.root.globals, tree.root.globals)

        game = GameActor()
        for node in tree_def.root.globals._children:
            self._build_node(game, node)

        print('SessionTree:')
        print([n for n in tree])

    def _build_node(self, owner, node_def):
        sess_entity = None
        if node_def.entity is not None:
            builder = Factory.Builders.get(type(node_def.entity))
            if not builder:
                logging.error(f'No builder is defined for type {type(node_def.entity)}.')
                return None
            sess_entity = builder.create(owner, node_def.entity)

        sess_node = Node(node_def.name, entity=sess_entity)
        self._register(node_def, sess_node)
        parent = self._find_session_parent(node_def)
        if parent is not None:
            parent.add_node(sess_node)

    @staticmethod
    def build_players(count):
        for i in range(count):
            yield Player(i)

    def _find_session_parent(self, def_node):
        """ Sets the correct parent for a session node based on the parent of its associated definition
        node `def_node`. """
        parent = self._nodedict.get(def_node.parent)
        if parent is None:
            logging.error(f'Parent not found for session node associated to {def_node}.')
        return parent

    def _register(self, def_node, sess_node):
        """ Registers that the session node `sess_node` was created from the definition node `def_node`. """
        self._nodedict[def_node] = sess_node
