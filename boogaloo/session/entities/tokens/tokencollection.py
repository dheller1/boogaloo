from ..entity import Entity


class TokenCollection(Entity):
    """ Collection of tokens which might be player-owned (e.g. gold coins or VP of a player) or a global token supply.
    """
    def __init__(self, token_type, start_amount=0, unlimited=False):
        super().__init__()
        self.token_type = token_type
        self.amount = start_amount
        self.unlimited = unlimited
