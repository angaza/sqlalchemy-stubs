from typing import Any, Optional, Union, Iterable, Tuple, TypeVar, Type, Generic, List, overload, Text
from .base import Executable as Executable, ColumnCollection
from .elements import (
    ColumnElement as ColumnElement, Grouping, ClauseList, ColumnElement, Over, WithinGroup, FunctionFilter, AsBoolean
)
from .selectable import FromClause as FromClause, Alias, Select
from . import util as sqlutil
from .visitors import VisitableType as VisitableType
from .type_api import TypeEngine
from .schema import Sequence
from . import sqltypes
from datetime import datetime, date, time
from ..engine.result import ResultProxy
from ..engine.base import Engine, Connection

_T = TypeVar('_T')

def register_function(identifier, fn, package: str = ...): ...

_FE = TypeVar('_FE', bound=FunctionElement)

class FunctionElement(Executable, ColumnElement[_T], FromClause, Generic[_T]):  # type: ignore
    # ColumnElement.foreign_keys() is not compatible with FromClause.foreign_keys()
    packagenames: Any = ...
    clause_expr: Grouping[Any] = ...
    def __init__(self, *clauses: Any, **kwargs: Any) -> None: ...
    # Return type of "columns" incompatible with supertype "FromClause"
    @property
    def columns(self) -> ColumnCollection: ...  # type: ignore
    @property
    def clauses(self) -> ClauseList: ...
    @overload
    def over(self, partition_by: Optional[Union[str, ColumnElement[Any], Iterable[Union[str, ColumnElement[Any]]]]] = ...,
             order_by: Optional[Union[str, ColumnElement[Any], Iterable[Union[str, ColumnElement[Any]]]]] = ...,
             range_: Optional[Tuple[Optional[int], Optional[int]]] = ...) -> Over[_T]: ...
    @overload
    def over(self, partition_by: Optional[Union[str, ColumnElement[Any], Iterable[Union[str, ColumnElement[Any]]]]] = ...,
             order_by: Optional[Union[str, ColumnElement[Any], Iterable[Union[str, ColumnElement[Any]]]]] = ...,
             rows: Optional[Tuple[Optional[int], Optional[int]]] = ...) -> Over[_T]: ...
    def within_group(self, *order_by: Union[str,
                                            ColumnElement[Any],
                                            Iterable[Union[str, ColumnElement[Any]]]]) -> WithinGroup[_T]: ...
    @overload
    def filter(self: _FE) -> _FE: ...
    @overload
    def filter(self, criteria: Any, *criterion: Any) -> FunctionFilter[_T]: ...
    def get_children(self, **kwargs: Any) -> Tuple[Grouping[Any]]: ...
    def within_group_type(self, within_group: Any) -> Any: ...
    def alias(self, name: Optional[str] = ..., flat: bool = ...) -> Alias: ...
    def select(self) -> Select: ...  # type: ignore  # incompatible with FromClause.select
    def scalar(self) -> Any: ...  # type: ignore  # incompatible with Executable.scalar
    def execute(self) -> ResultProxy: ...  # type: ignore  # incompatible with Executable.execute
    def self_group(self: _FE, against: Optional[Any] = ...) -> Union[AsBoolean, Grouping[_T], _FE]: ...

class _FunctionGenerator(object):
    opts: Any = ...
    def __init__(self, **opts: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __call__(self, *c: Any, **kwargs: Any) -> Function[Any]: ...

func: _FunctionGenerator = ...
modifier: _FunctionGenerator = ...

class Function(FunctionElement[_T]):
    __visit_name__: str = ...
    packagenames: Any = ...
    name: str = ...
    type: TypeEngine[_T] = ...
    def __init__(self, name: str, *clauses: Any, **kw: Any) -> None: ...

class _GenericMeta(VisitableType):
    def __init__(cls, clsname, bases, clsdict) -> None: ...

class GenericFunction(Function[_T], metaclass=_GenericMeta):
    coerce_arguments: bool = ...
    packagenames: Any = ...
    clause_expr: Grouping[Any] = ...
    type: TypeEngine[_T] = ...
    @overload
    def __init__(self, *args: ColumnElement[Any], bind: Optional[Union[Engine, Connection]] = ...,
                 type_: Type[TypeEngine[_T]]) -> None: ...
    @overload
    def __init__(self, *args: ColumnElement[Any], bind: Optional[Union[Engine, Connection]] = ...,
                 type_: TypeEngine[_T]) -> None: ...
    @overload
    def __init__(self, *args: Union[_T, ColumnElement[_T]], bind: Optional[Union[Engine, Connection]] = ...) -> None: ...
    @overload
    def __init__(self, *, _parsed_args: List[ColumnElement[Any]], bind: Optional[Union[Engine, Connection]] = ...,
                 type_: Type[TypeEngine[_T]]) -> None: ...
    @overload
    def __init__(self, *, _parsed_args: List[ColumnElement[Any]], bind: Optional[Union[Engine, Connection]] = ...,
                 type_: TypeEngine[_T]) -> None: ...
    @overload
    def __init__(self, *, _parsed_args: List[ColumnElement[_T]], bind: Optional[Union[Engine, Connection]] = ...) -> None: ...

class next_value(GenericFunction[_T]):
    type: TypeEngine[_T] = ...
    name: str = ...
    sequence: Sequence[_T] = ...
    def __init__(self, seq: Sequence[_T], **kw) -> None: ...

class AnsiFunction(GenericFunction[_T]):
    def __init__(self, **kwargs) -> None: ...

class ReturnTypeFromArgs(GenericFunction[_T]):
    def __init__(self, *args, **kwargs) -> None: ...

class coalesce(ReturnTypeFromArgs[Any]): ...
class max(ReturnTypeFromArgs[Any]): ...
class min(ReturnTypeFromArgs[Any]): ...
class sum(ReturnTypeFromArgs[Any]): ...

class now(GenericFunction[datetime]): ...

class concat(GenericFunction[Text]): ...

class char_length(GenericFunction[int]): ...

class random(GenericFunction[_T]): ...

class count(GenericFunction[int]):
    def __init__(self, expression: Optional[Any] = ..., **kwargs: Any) -> None: ...

class current_date(AnsiFunction[date]): ...

class current_time(AnsiFunction[time]): ...

class current_timestamp(AnsiFunction[datetime]): ...

class current_user(AnsiFunction[Text]): ...

class localtime(AnsiFunction[datetime]): ...

class localtimestamp(AnsiFunction[datetime]): ...

class session_user(AnsiFunction[Text]): ...

class sysdate(AnsiFunction[datetime]): ...

class user(AnsiFunction[Text]): ...

class array_agg(GenericFunction[List[_T]], Generic[_T]):
    @overload
    def __init__(self, *args: ColumnElement[Any], bind: Optional[Union[Engine, Connection]] = ...,
                 type_: Type[TypeEngine[_T]]) -> None: ...
    @overload
    def __init__(self, *args: ColumnElement[Any], bind: Optional[Union[Engine, Connection]] = ...,
                 type_: TypeEngine[_T]) -> None: ...
    @overload
    def __init__(self, *args: ColumnElement[_T], bind: Optional[Union[Engine, Connection]] = ...) -> None: ...
    @overload
    def __init__(self, *args: ColumnElement[Any], bind: Optional[Union[Engine, Connection]] = ...,
                 type_: Type[TypeEngine[_T]], _default_array_type: Type[TypeEngine[Any]]) -> None: ...
    @overload
    def __init__(self, *args: ColumnElement[Any], bind: Optional[Union[Engine, Connection]] = ...,
                 type_: TypeEngine[_T], _default_array_type: Type[TypeEngine[Any]]) -> None: ...
    @overload
    def __init__(self, *args: ColumnElement[_T], bind: Optional[Union[Engine, Connection]] = ...,
                 _default_array_type: Type[TypeEngine[Any]]) -> None: ...

class OrderedSetAgg(GenericFunction[_T]):
    array_for_multi_clause: bool = ...
    def within_group_type(self, within_group: WithinGroup[_T]) -> Union[TypeEngine[_T], sqltypes.ARRAY[_T]]: ...

class mode(OrderedSetAgg[_T]):
    def within_group_type(self, within_group: WithinGroup[_T]) -> TypeEngine[_T]: ...

class percentile_cont(OrderedSetAgg[Any]): ...

class percentile_disc(OrderedSetAgg[Any]): ...

class rank(GenericFunction[int]): ...

class dense_rank(GenericFunction[int]): ...

class percent_rank(GenericFunction[float]): ...

class cume_dist(GenericFunction[float]): ...
