# Stubs for sqlalchemy.orm.path_registry (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .base import class_mapper as class_mapper

log = ...  # type: Any

class PathRegistry(object):
    is_token = ...  # type: bool
    is_root = ...  # type: bool
    def __eq__(self, other): ...
    def set(self, attributes, key, value): ...
    def setdefault(self, *args, **kwargs): ...
    def get(self, *args, **kwargs): ...
    def __len__(self): ...
    @property
    def length(self): ...
    def pairs(self): ...
    def contains_mapper(self, mapper): ...
    def contains(self, attributes, key): ...
    def __reduce__(self): ...
    def serialize(self): ...
    @classmethod
    def deserialize(cls, path): ...
    @classmethod
    def per_mapper(cls, mapper): ...
    @classmethod
    def coerce(cls, raw): ...
    def token(self, token): ...
    def __add__(self, other): ...

class RootRegistry(PathRegistry):
    path = ...  # type: Any
    has_entity = ...  # type: bool
    is_aliased_class = ...  # type: bool
    is_root = ...  # type: bool
    def __getitem__(self, entity): ...

class TokenRegistry(PathRegistry):
    token = ...  # type: Any
    parent = ...  # type: Any
    path = ...  # type: Any
    def __init__(self, parent, token) -> None: ...
    has_entity = ...  # type: bool
    is_token = ...  # type: bool
    def generate_for_superclasses(self): ...
    def __getitem__(self, entity): ...

class PropRegistry(PathRegistry):
    prop = ...  # type: Any
    parent = ...  # type: Any
    path = ...  # type: Any
    def __init__(self, parent, prop) -> None: ...
    @property
    def has_entity(self): ...
    @property
    def entity(self): ...
    @property
    def mapper(self): ...
    @property
    def entity_path(self): ...
    def __getitem__(self, entity): ...

class EntityRegistry(PathRegistry, dict):
    is_aliased_class = ...  # type: bool
    has_entity = ...  # type: bool
    key = ...  # type: Any
    parent = ...  # type: Any
    entity = ...  # type: Any
    path = ...  # type: Any
    entity_path = ...  # type: Any
    def __init__(self, parent, entity) -> None: ...
    @property
    def mapper(self): ...
    def __bool__(self): ...
    __nonzero__ = ...  # type: Any
    def __getitem__(self, entity): ...
    def __missing__(self, key): ...