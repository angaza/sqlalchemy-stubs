# Stubs for sqlalchemy.dialects.postgresql.pypostgresql (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ... import types as sqltypes
from .base import PGDialect as PGDialect, PGExecutionContext as PGExecutionContext

class PGNumeric(sqltypes.Numeric):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class PGExecutionContext_pypostgresql(PGExecutionContext): ...

class PGDialect_pypostgresql(PGDialect):
    driver = ...  # type: str
    supports_unicode_statements = ...  # type: bool
    supports_unicode_binds = ...  # type: bool
    description_encoding = ...  # type: Any
    default_paramstyle = ...  # type: str
    supports_sane_rowcount = ...  # type: bool
    supports_sane_multi_rowcount = ...  # type: bool
    execution_ctx_cls = ...  # type: Any
    colspecs = ...  # type: Any
    @classmethod
    def dbapi(cls): ...
    def dbapi_exception_translation_map(self): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect = ...  # type: Any
