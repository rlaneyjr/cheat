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
    url = 'https://github.com/rlaneyjr/cheat',
    packages = [
        'cheats',
        'cheats.cheatsheets',
        'cheats.test',
    ],
    install_requires = ['docopt', 'pygments'],
    package_data = {
        'cheats.cheatsheets': [f for f in os.listdir('cheats/cheatsheets') if '.' not in f]
    },
    entry_points = {
        'console_scripts': ['cheat = cheat'],
    },
)
