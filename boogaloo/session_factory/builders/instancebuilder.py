from boogaloo.session.actors import Actor
from boogaloo.session.entities.entity import Entity


class InstanceBuilder:
    """ Base class for builder classes used to create `session` objects from `definition` objects.
    InstanceBuilder subclasses specify their source and target types, and should then implement the _create() method
    to instantiate a target object from a given source/definition object. """
    def __init__(self, sourcetype, targettype):
        assert issubclass(targettype, Entity)
        self.sourcetype = sourcetype
        self.targettype = targettype

    def create(self, owner, definition):
        """ Creates and returns a targettype object based on the source_object, with the given owner.
        :param owner: Actor instance which shall own the created object.
        :param definition: EntityDefinition instance which describe the object to be created. """
        assert isinstance(definition, self.sourcetype)
        assert isinstance(owner, Actor)
        target_obj = self._create(definition)
        target_obj.owner = owner
        return target_obj

    def _create(self, definition):
        raise NotImplementedError
