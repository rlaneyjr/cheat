from distutils.core import setup
import os

setup(
    name         = 'cheat',
    version      = '1.0',
    author       = 'Ricky Laney',
    author_email = 'rlaneyjr@gmail.com',
    license      = 'GPL3',
    description  = 'This is my version of cheat completely stolen from Chris Allen Lane'
    'cheat allows you to create and view interactive cheatsheets '
    'on the command-line. It was designed to help remind *nix system '
    'administrators of options for commands that they use frequently, but not '
    'frequently enough to remember.',
    url          = 'https://github.com/rlaneyjr/cheat',
    packages     = [
        'cheat',
        'cheat.cheatsheets',
        'cheat.test',
    ],
    package_data = {
        'cheat.cheatsheets': [f for f in os.listdir('cheat/cheatsheets') if '.' not in f]
    },
    scripts          = ['bin/cheat'],
    install_requires = [
        'docopt >= 0.6.1',
        'pygments >= 1.6.0',
    ]
)
