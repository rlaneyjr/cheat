# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'DESCRIPTION.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'cheat',
    version = '1.0',
    author = 'Ricky Laney',
    author_email = 'rlaneyjr@gmail.com',
    license = 'GPL3',
    description = 'cheat allows you to create and view interactive cheatsheets',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/rlaneyjr/cheat',
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #py_modules=["cheat/cheat"],
    #
    packages = ['cheat', 'cheat.cheatsheets', 'cheat.test'],
    install_requires = ['docopt >= 0.6.2', 'Pygments >= 2.2.0'],
    package_data = {
        'cheat.cheatsheets': [f for f in os.listdir('cheat/cheatsheets') if '.' not in f]
    },
    entry_points = {
        'console_scripts': ['cheat=bin.cheat:main'],
    },
    #scripts = ['bin/cheat'],
)

