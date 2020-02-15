from enum import Enum


class Visibility(Enum):
    All = 1  # Visible to all actors
    Owner = 2  # Visible only to owner
    Nobody = 3  # Visible to nobody
