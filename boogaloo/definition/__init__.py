""" The definition module contains classes which can be used to define the components which make up the game and
their relations. Instances of these classes describe the general ruleset of a game, they do not refer to concrete
objects _in_ a specific game yet.

Users should facilitate this module to define how their game works, then create a concrete game session from it
(using the `session_factory` module) which instantiates all required objects according to the defined ruleset.
"""

# Module must not depend on: session
