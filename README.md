# sqlalchemy-stubs

## About

This repository contains external type annotations (see
[PEP 484](https://www.python.org/dev/peps/pep-0484/)) for the
[SQLAlchemy](https://www.sqlalchemy.org/) package. Such type annotations are normally included
in [typeshed](https://www.github.com/python/typeshed), but SQLAlchemy's annotations were
frequently problematic and have therefore been deleted from typeshed. This repo provides SQLAlchemy
stubs with some issues fixed for those who find them useful. Hopefully it can eventually be merged
back into typeshed.

This package contains [type stubs](https://www.python.org/dev/peps/pep-0561/) and a
[mypy plugin](https://mypy.readthedocs.io/en/latest/extending_mypy.html#extending-mypy-using-plugins)
to provide more precise static types and type inference for
[SQLAlchemy framework](http://docs.sqlalchemy.org/en/latest/). SQLAlchemy uses some
Python "magic" that makes having precise types for some code patterns problematic.
This is why we need to accompany the stubs with mypy plugins. The final goal is to
be able to get precise types for most common patterns. Currently, basic operations
with models are supported. A simple example:
```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

To use these stubs, clone this repo and point your type checker to it. For example, to use them in
[mypy](http://github.com/python/mypy), you can set the `$MYPYPATH` environment variable or set
`mypy_path = /path/to/sqlalchemy-stubs` in your `mypy.ini`.

This fork is a combination of an original fork from https://github.com/JelleZijlstra/sqlalchemy-stubs
customized with a few Angaza commits, then merged with updated stub code from
https://github.com/dropbox/sqlalchemy-stubs.


**To update moving forward**, merge in the relevant changes
from https://github.com/dropbox/sqlalchemy-stubs


## Example

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

user = User(id=42, name=42)  # Error: Incompatible type for "name" of "User"
                             # (got "int", expected "Optional[str]")
user.id  # Inferred type is "int"
User.name  # Inferred type is "Column[Optional[str]]"
```

Some auto-generated attributes are added to models. Simple relationships
are supported but require models to be imported:
```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.address import Address

...

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship('Address')  # OK, mypy understands string references.
```

The next step is to support precise types for table definitions (e.g.
inferring `Column[Optional[str]]` for `users.c.name`, currently it is just
`Column[Any]`), and precise types for results of queries made using `query()`
and `select()`.

## Installation
Install latest published version as:
```
pip install -U sqlalchemy-stubs
```

*Important*: you need to enable the plugin in your mypy config file:
```
[mypy]
plugins = sqlmypy
```

To install the development version of the package:
```
git clone https://github.com/dropbox/sqlalchemy-stubs
cd sqlalchemy-stubs
pip install -U .
```

## Development Setup

First, clone the repo and cd into it, like in _Installation_, then:
```
git submodule update --init --recursive
pip install -r dev-requirements.txt
```

Then, to run the tests, simply:
```
pytest
```

## Development status

The package is currently in alpha stage. See [issue tracker](https://github.com/dropbox/sqlalchemy-stubs/issues)
for bugs and missing features. If you want to contribute, a good place to start is
[`help-wanted` label](https://github.com/dropbox/sqlalchemy-stubs/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22).

Currently, some basic use cases like inferring model field types are supported.
The long term goal is to be able to infer types for more complex situations
like correctly inferring columns in most compound queries.

External contributions to the project should be subject to
[Dropbox Contributor License Agreement (CLA)](https://opensource.dropbox.com/cla/).

--------------------------------
Copyright (c) 2018 Dropbox, Inc.
