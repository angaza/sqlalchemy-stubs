# Stubs for sqlalchemy.dialects.oracle.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from sqlalchemy.sql import compiler, elements
from sqlalchemy.engine import default
from sqlalchemy.sql import util as sql_util
from sqlalchemy.sql import operators as sql_operators
from sqlalchemy import types as sqltypes, schema as sa_schema
from sqlalchemy.types import VARCHAR as VARCHAR, NVARCHAR as NVARCHAR, CHAR as CHAR, \
    BLOB as BLOB, CLOB as CLOB, TIMESTAMP as TIMESTAMP, FLOAT as FLOAT

RESERVED_WORDS = ...  # type: Any
NO_ARG_FNS = ...  # type: Any

class RAW(sqltypes._Binary):
    __visit_name__ = ...  # type: str

OracleRaw = ...  # type: Any

class NCLOB(sqltypes.Text):
    __visit_name__ = ...  # type: str

class VARCHAR2(VARCHAR):
    __visit_name__ = ...  # type: str

NVARCHAR2 = ...  # type: Any

class NUMBER(sqltypes.Numeric):
    __visit_name__ = ...  # type: str
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: Optional[Any] = ...) -> None: ...
    def adapt(self, impltype): ...

class DOUBLE_PRECISION(sqltypes.Numeric):
    __visit_name__ = ...  # type: str
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: Optional[Any] = ...) -> None: ...

class BFILE(sqltypes.LargeBinary):
    __visit_name__ = ...  # type: str

class LONG(sqltypes.Text):
    __visit_name__ = ...  # type: str

class DATE(sqltypes.DateTime):
    __visit_name__ = ...  # type: str

class INTERVAL(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str
    day_precision = ...  # type: Any
    second_precision = ...  # type: Any
    def __init__(self, day_precision: Optional[Any] = ..., second_precision: Optional[Any] = ...) -> None: ...

class ROWID(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

class _OracleBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi): ...

colspecs = ...  # type: Any
ischema_names = ...  # type: Any

class OracleTypeCompiler(compiler.GenericTypeCompiler):
    def visit_datetime(self, type_, **kw): ...
    def visit_float(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_INTERVAL(self, type_, **kw): ...
    def visit_LONG(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_DOUBLE_PRECISION(self, type_, **kw): ...
    def visit_NUMBER(self, type_, **kw): ...
    def visit_string(self, type_, **kw): ...
    def visit_VARCHAR2(self, type_, **kw): ...
    def visit_NVARCHAR2(self, type_, **kw): ...
    visit_NVARCHAR = ...  # type: Any
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_big_integer(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_RAW(self, type_, **kw): ...
    def visit_ROWID(self, type_, **kw): ...

class OracleCompiler(compiler.SQLCompiler):
    compound_keywords = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def visit_mod_binary(self, binary, operator, **kw): ...
    def visit_now_func(self, fn, **kw): ...
    def visit_char_length_func(self, fn, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def get_cte_preamble(self, recursive): ...
    def get_select_hint_text(self, byfroms): ...
    def function_argspec(self, fn, **kw): ...
    def default_from(self): ...
    def visit_join(self, join, **kwargs): ...
    def visit_outer_join_column(self, vc, **kw): ...
    def visit_sequence(self, seq): ...
    def get_render_as_alias_suffix(self, alias_name_text): ...
    def returning_clause(self, stmt, returning_cols): ...
    def visit_select(self, select, **kwargs): ...
    def limit_clause(self, select, **kw): ...
    def for_update_clause(self, select, **kw): ...

class OracleDDLCompiler(compiler.DDLCompiler):
    def define_constraint_cascades(self, constraint): ...
    def visit_create_index(self, create): ...
    def post_create_table(self, table): ...

class OracleIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = ...  # type: Any
    illegal_initial_characters = ...  # type: Any
    def format_savepoint(self, savepoint): ...

class OracleExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq, type_): ...

class OracleDialect(default.DefaultDialect):
    name = ...  # type: str
    supports_alter = ...  # type: bool
    supports_unicode_statements = ...  # type: bool
    supports_unicode_binds = ...  # type: bool
    max_identifier_length = ...  # type: int
    supports_sane_rowcount = ...  # type: bool
    supports_sane_multi_rowcount = ...  # type: bool
    supports_simple_order_by_label = ...  # type: bool
    supports_sequences = ...  # type: bool
    sequences_optional = ...  # type: bool
    postfetch_lastrowid = ...  # type: bool
    default_paramstyle = ...  # type: str
    colspecs = ...  # type: Any
    ischema_names = ...  # type: Any
    requires_name_normalize = ...  # type: bool
    supports_default_values = ...  # type: bool
    supports_empty_insert = ...  # type: bool
    statement_compiler = ...  # type: Any
    ddl_compiler = ...  # type: Any
    type_compiler = ...  # type: Any
    preparer = ...  # type: Any
    execution_ctx_cls = ...  # type: Any
    reflection_options = ...  # type: Any
    construct_arguments = ...  # type: Any
    use_ansi = ...  # type: Any
    optimize_limits = ...  # type: Any
    use_binds_for_limits = ...  # type: Any
    exclude_tablespaces = ...  # type: Any
    def __init__(self, use_ansi: bool = ..., optimize_limits: bool = ..., use_binds_for_limits: bool = ..., exclude_tablespaces: Any = ..., **kwargs) -> None: ...
    implicit_returning = ...  # type: Any
    def initialize(self, connection): ...
    def do_release_savepoint(self, connection, name): ...
    def has_table(self, connection, table_name, schema: Optional[Any] = ...): ...
    def has_sequence(self, connection, sequence_name, schema: Optional[Any] = ...): ...
    def normalize_name(self, name): ...
    def denormalize_name(self, name): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, schema: Optional[Any] = ..., **kw): ...
    def get_temp_table_names(self, connection, **kw): ...
    def get_view_names(self, connection, schema: Optional[Any] = ..., **kw): ...
    def get_table_options(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_columns(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_indexes(self, connection, table_name, schema: Optional[Any] = ..., resolve_synonyms: bool = ..., dblink: str = ..., **kw): ...
    def get_pk_constraint(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_foreign_keys(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_view_definition(self, connection, view_name, schema: Optional[Any] = ..., resolve_synonyms: bool = ..., dblink: str = ..., **kw): ...

class _OuterJoinColumn(elements.ClauseElement):
    __visit_name__ = ...  # type: str
    column = ...  # type: Any
    def __init__(self, column) -> None: ...
