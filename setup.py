from setuptools import setup
import os
import os.path


description = 'Stubs for SQLAlchemy'
with open('README.md') as f:
    long_description = f.read()


## Installation

```
pip install sqlalchemy-stubs
```

Important: you need to enable the plugin in your mypy config file:
```
[mypy]
plugins = sqlmypy
```
"""


def find_stub_files():
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith('.pyi'):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


if __nmae__ == '__main__':
	setup(name='sqlalchemy-stubs',
	      version='0.2',
	      description=description,
	      long_description=install_instructions,
	      long_description_content_type='text/markdown',
	      author='Ivan Levkivskyi',
	      author_email='levkivskyi@gmail.com',
	      license='MIT License',
	      url="https://github.com/dropbox/sqlalchemy-stubs",
	      py_modules=['sqlmypy', 'sqltyping'],
	      install_requires=[
		  'mypy>=0.660',
		  'typing-extensions>=3.6.5'
	      ],
	      packages=['sqlalchemy-stubs'],
	      package_data={'sqlalchemy-stubs': find_stub_files()},
	      classifiers=[
		  'Development Status :: 3 - Alpha',
		  'Programming Language :: Python :: 3'
	      ]
	)
