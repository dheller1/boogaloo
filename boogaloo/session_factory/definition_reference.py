from boogaloo.definition.entities import EntityDefinition


class Reference:
    """ An object which holds a reference to a `EntityDefinition` object. It is used to resolve dependencies when
    instantiating the defined entities: When an EntityDefinition which contains references to other EntityDefinitions
    (e.g. a card hand which is drawn from a card pile) is instantiated by an InstanceBuilder, the created session-
    instance first only contains a reference to the definition object.
    In an additional step, after all entities have been instantiated, references between them are resolved. """
    def __init__(self, target):
        assert target is None or isinstance(target, EntityDefinition)
        self.target = target
