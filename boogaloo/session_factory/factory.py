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

    @staticmethod
    def build_tree(tree_def, num_players):
        tree = SessionTree()

        game = GameActor()
        players = list(Factory.build_players(num_players))

        for node in tree_def.root.globals:
            Factory.build_node(game, node)

        for node in tree_def.root.per_player:
            pass

    @staticmethod
    def build_node(owner, node_def):
        if node_def.entity is not None:
            builder = Factory.Builders.get(type(node_def.entity))
            if not builder:
                logging.error(f'No builder is defined for type {type(node_def.entity)}.')
                return None

            return builder.create(owner, node_def.entity)

    @staticmethod
    def build_players(count):
        for i in range(count):
            yield Player(i)
