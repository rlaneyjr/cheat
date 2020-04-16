# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

def get_long_desc():
    # Get the long description from the relevant file
    long_desc_file = os.path.join(here, 'DESCRIPTION.md')
    if os.path.exists(long_desc_file):
        with open(long_desc_file, encoding='utf-8') as f:
            return f.read()
    else:
        return description

setup(
    name = 'cheat',
    version = '2.2',
    author = 'Ricky Laney',
    author_email = 'rlaneyjr@gmail.com',
    license = 'GPL3',
    description = 'cheat allows you to create and view interactive cheatsheets',
    long_description = get_long_desc(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/rlaneyjr/cheat',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #py_modules=["cheat/cheat"],
    #
    # packages = ['src.cheat', 'src.cheat.cheatsheets', 'src.cheat.test'],
    packages=find_packages(),
    include_package_data=True,
    install_requires = ['docopt >= 0.6.2', 'Pygments >= 2.2.0'],
    package_data = {
        'src.cheat.cheatsheets': [f for f in os.listdir('src/cheat/cheatsheets') if '.' not in f]
    },
    entry_points = '''
        [console_scripts]
        cheat=src.cheat:main
    ''',
    # scripts = ['src/cheat'],
    project_urls={
        'Bug Reports': 'https://github.com/rlaney/cheat/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/rlaneyjr',
        'Source': 'https://github.com/rlaneyjr/cheat/',
    },
)

