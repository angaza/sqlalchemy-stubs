# Stubs for sqlalchemy.ext.indexable (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ..ext.hybrid import hybrid_property

class index_property(hybrid_property):
    attr_name = ...  # type: Any
    index = ...  # type: Any
    default = ...  # type: Any
    datatype = ...  # type: Any
    onebased = ...  # type: Any
    def __init__(self, attr_name, index, default: Any = ..., datatype: Optional[Any] = ..., mutable: bool = ..., onebased: bool = ...) -> None: ...
    def fget(self, instance): ...
    def fset(self, instance, value): ...
    def fdel(self, instance): ...
    def expr(self, model): ...