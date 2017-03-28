# Stubs for sqlalchemy.sql.util (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import visitors
from .base import ColumnSet as ColumnSet
from .elements import BindParameter as BindParameter, ColumnClause as ColumnClause, ColumnElement as ColumnElement, Null as Null, UnaryExpression as UnaryExpression, literal_column as literal_column, Label as Label, _label_reference as _label_reference, _textual_label_reference as _textual_label_reference
from .selectable import ScalarSelect as ScalarSelect, Join as Join, FromClause as FromClause, FromGrouping as FromGrouping
from .schema import Column as Column
from .ddl import sort_tables as sort_tables

join_condition = ...  # type: Any

def find_join_source(clauses, join_to): ...
def visit_binary_product(fn, expr): ...
def find_tables(clause, check_columns: bool = ..., include_aliases: bool = ..., include_joins: bool = ..., include_selects: bool = ..., include_crud: bool = ...): ...
def unwrap_order_by(clause): ...
def unwrap_label_reference(element): ...
def expand_column_list_from_order_by(collist, order_by): ...
def clause_is_present(clause, search): ...
def surface_selectables(clause): ...
def surface_column_elements(clause): ...
def selectables_overlap(left, right): ...
def bind_values(clause): ...

class _repr_base(object):
    def trunc(self, value): ...

class _repr_row(_repr_base):
    row = ...  # type: Any
    max_chars = ...  # type: Any
    def __init__(self, row, max_chars: int = ...) -> None: ...

class _repr_params(_repr_base):
    params = ...  # type: Any
    batches = ...  # type: Any
    max_chars = ...  # type: Any
    def __init__(self, params, batches, max_chars: int = ...) -> None: ...

def adapt_criterion_to_null(crit, nulls): ...
def splice_joins(left, right, stop_on: Optional[Any] = ...): ...
def reduce_columns(columns, *clauses, **kw): ...
def criterion_as_pairs(expression, consider_as_foreign_keys: Optional[Any] = ..., consider_as_referenced_keys: Optional[Any] = ..., any_operator: bool = ...): ...

class ClauseAdapter(visitors.ReplacingCloningVisitor):
    __traverse_options__ = ...  # type: Any
    selectable = ...  # type: Any
    include_fn = ...  # type: Any
    exclude_fn = ...  # type: Any
    equivalents = ...  # type: Any
    adapt_on_names = ...  # type: Any
    def __init__(self, selectable, equivalents: Optional[Any] = ..., include_fn: Optional[Any] = ..., exclude_fn: Optional[Any] = ..., adapt_on_names: bool = ..., anonymize_labels: bool = ...) -> None: ...
    def replace(self, col): ...

class ColumnAdapter(ClauseAdapter):
    columns = ...  # type: Any
    adapt_required = ...  # type: Any
    allow_label_resolve = ...  # type: Any
    def __init__(self, selectable, equivalents: Optional[Any] = ..., chain_to: Optional[Any] = ..., adapt_required: bool = ..., include_fn: Optional[Any] = ..., exclude_fn: Optional[Any] = ..., adapt_on_names: bool = ..., allow_label_resolve: bool = ..., anonymize_labels: bool = ...) -> None: ...
    class _IncludeExcludeMapping(object):
        parent = ...  # type: Any
        columns = ...  # type: Any
        def __init__(self, parent, columns) -> None: ...
        def __getitem__(self, key): ...
    def wrap(self, adapter): ...
    def traverse(self, obj): ...
    adapt_clause = ...  # type: Any
    adapt_list = ...  # type: Any