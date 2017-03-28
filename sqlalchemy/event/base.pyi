# Stubs for sqlalchemy.event.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .attr import _JoinedListener as _JoinedListener, _EmptyListener as _EmptyListener, _ClsLevelDispatch as _ClsLevelDispatch

class _UnpickleDispatch(object):
    def __call__(self, _instance_cls): ...

class _Dispatch(object):
    def __init__(self, parent, instance_cls: Optional[Any] = ...) -> None: ...
    def __getattr__(self, name): ...
    def __reduce__(self): ...

class _EventMeta(type):
    def __init__(cls, classname, bases, dict_) -> None: ...

class Events(metaclass=_EventMeta): ...

class _JoinedDispatcher(object):
    local = ...  # type: Any
    parent = ...  # type: Any
    def __init__(self, local, parent) -> None: ...
    def __getattr__(self, name): ...

class dispatcher(object):
    dispatch_cls = ...  # type: Any
    events = ...  # type: Any
    def __init__(self, events) -> None: ...
    def __get__(self, obj, cls): ...