# Stubs for sqlalchemy.ext.declarative.clsregistry (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ...orm.properties import ColumnProperty as ColumnProperty
from ...orm import class_mapper as class_mapper, interfaces as interfaces

def add_class(classname, cls): ...

class _MultipleClassMarker(object):
    on_remove = ...  # type: Any
    contents = ...  # type: Any
    def __init__(self, classes, on_remove: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...
    def attempt_get(self, path, key): ...
    def add_item(self, item): ...

class _ModuleMarker(object):
    parent = ...  # type: Any
    name = ...  # type: Any
    contents = ...  # type: Any
    mod_ns = ...  # type: Any
    path = ...  # type: Any
    def __init__(self, name, parent) -> None: ...
    def __contains__(self, name): ...
    def __getitem__(self, name): ...
    def resolve_attr(self, key): ...
    def get_module(self, name): ...
    def add_class(self, name, cls): ...

class _ModNS(object):
    def __init__(self, parent) -> None: ...
    def __getattr__(self, key): ...

class _GetColumns(object):
    cls = ...  # type: Any
    def __init__(self, cls) -> None: ...
    def __getattr__(self, key): ...

class _GetTable(object):
    key = ...  # type: Any
    metadata = ...  # type: Any
    def __init__(self, key, metadata) -> None: ...
    def __getattr__(self, key): ...

class _class_resolver(object):
    cls = ...  # type: Any
    prop = ...  # type: Any
    arg = ...  # type: Any
    fallback = ...  # type: Any
    def __init__(self, cls, prop, fallback, arg) -> None: ...
    def __call__(self): ...