#!/usr/bin/env python
#title:             ren-may.py
#description:       ren-may
#author:            Ricky
#date:              20180831
#version:           1
#usage:             python ren-may.py or ./ren-may.py
#notes:
#python_version:    3.6.5
#==============================================================================

import os
from shutil import copyfile as cp

BASE_DIR = "/Users/rlaney/.cheat/NEW/MayccollUtils"
RES_DIR = "/Users/rlaney/.cheat/NEW/results"
IGNORED_DIRS = ['Site', 'Localhost']


def create_results(directory):
    for d in os.scandir(directory):
        if d.name == "results" and d.is_dir():
            os.rmdir(d.path)
    results = os.mkdir(os.path.join(directory, "results"))
    print("Created results folder")
    return results


def print_tree(directory):
    # traverse BASE_DIR directory, and list directories as dirs and files as files
    for base, dirs, files in os.walk(directory):
        path_list = base.split(os.sep)
        print((len(path_list) - 1) * '---', os.path.basename(base))
        for file in files:
            print(len(path_list) * '---', file)
    return print("Tree completed")


def move_files(directory, results):
    dir_list = []
    for d in os.scandir(directory):
        if d.name in IGNORED_DIRS or not d.is_dir():
            break
        else:
            dir_list.append(d.name)
    for dr in dir_list:
        path = os.path.join(directory, dr)
        if dr == "Nodejs":
            cp(os.path.join(path, "exec_unix.node.js"), os.path.join(results, "nodejs.md"))
        elif dr == "Bitnami":
            cp(os.path.join(path, "Nginx.md"), os.path.join(results, "bitnami.md"))
        elif dr == "Php":
            cp(os.path.join(path, "test.md"), os.path.join(results, "php.md"))
        elif dr == "Use Markdown":
            cp(os.path.join(path, "README.md"), os.path.join(results, "markdown.md"))
        else:
            cp(os.path.join(path, "README.md"), os.path.join(results, (dr.lower() + ".md")))

if __name__ == "__main__":
    results = create_results(BASE_DIR)
    print_tree(BASE_DIR)
    move_files(BASE_DIR, results)


'''
# traverse BASE_DIR directory, and list directories as dirs and files as files
for base, dirs, files in os.walk(BASE_DIR):


------------------ Nodejs
--------------------- exec_unix.node.js
------------------ Bitnami
--------------------- Nginx.md
------------------ Php
--------------------- test.md
------------------ Use Markdown
--------------------- README.md

/Users/rlaney/.cheat/NEW/MayccollUtils
['Firefox', 'Lamp', 'Redmine', 'Nodejs', 'Docker', 'Etherpad', 'Gitlab', 'Drupal', 'Gulp', 'Wordpress', 'Css', 'Less', 'Atom', 'Sublime-Text', 'Bitnami', 'OwnCloud', 'Youtube', 'Regex', 'Php', 'Bash', 'Ansible', 'FruityWifi', 'openVpn', 'Nginx', 'Use Markdown', 'Rocket.Chat', 'Mysql', 'Site', 'Localhost', 'Synergy', 'Javascript', 'Puppet', 'Brimir', 'Ruby', 'Remote']
['README.md', 'Firma.txt']
--------------- MayccollUtils
------------------ README.md
------------------ Firma.txt
/Users/rlaney/.cheat/NEW/MayccollUtils/Firefox
[]
['README.md']
------------------ Firefox
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Lamp
[]
['README.md']
------------------ Lamp
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Redmine
[]
['README.md']
------------------ Redmine
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Nodejs
[]
['exec_unix.node.js', 'test.sh']
------------------ Nodejs
--------------------- exec_unix.node.js
--------------------- test.sh
/Users/rlaney/.cheat/NEW/MayccollUtils/Docker
[]
['README.md']
------------------ Docker
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Etherpad
[]
['README.md']
------------------ Etherpad
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Gitlab
[]
['README.md']
------------------ Gitlab
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Drupal
[]
['README.md', '.htaccess']
------------------ Drupal
--------------------- README.md
--------------------- .htaccess
/Users/rlaney/.cheat/NEW/MayccollUtils/Gulp
[]
['README.md', 'gulpfile.js']
------------------ Gulp
--------------------- README.md
--------------------- gulpfile.js
/Users/rlaney/.cheat/NEW/MayccollUtils/Wordpress
[]
['README.md', 'wp_migrate.php']
------------------ Wordpress
--------------------- README.md
--------------------- wp_migrate.php
/Users/rlaney/.cheat/NEW/MayccollUtils/Css
[]
['README.md']
------------------ Css
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Less
[]
['media.less', 'clear.fix.less', 'README.md', 'links.less']
------------------ Less
--------------------- media.less
--------------------- clear.fix.less
--------------------- README.md
--------------------- links.less
/Users/rlaney/.cheat/NEW/MayccollUtils/Atom
[]
['README.md']
------------------ Atom
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Sublime-Text
[]
['Preferences.sublime-settings', 'Default(Linux).sublime-keymap', 'README.md']
------------------ Sublime-Text
--------------------- Preferences.sublime-settings
--------------------- Default(Linux).sublime-keymap
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Bitnami
[]
['Nginx.md']
------------------ Bitnami
--------------------- Nginx.md
/Users/rlaney/.cheat/NEW/MayccollUtils/OwnCloud
[]
['README.md']
------------------ OwnCloud
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Youtube
[]
['README.md']
------------------ Youtube
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Regex
[]
['README.md']
------------------ Regex
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Php
[]
['include.php', 'short_tag_remove.sh', 'test.md']
------------------ Php
--------------------- include.php
--------------------- short_tag_remove.sh
--------------------- test.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Bash
[]
['README.md']
------------------ Bash
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Ansible
[]
['README.md']
------------------ Ansible
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/FruityWifi
[]
['README.md']
------------------ FruityWifi
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/openVpn
[]
['README.md']
------------------ openVpn
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Nginx
[]
['README.md']
------------------ Nginx
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Use Markdown
[]
['data-markdown.user.js', 'README.md', 'example.html']
------------------ Use Markdown
--------------------- data-markdown.user.js
--------------------- README.md
--------------------- example.html
/Users/rlaney/.cheat/NEW/MayccollUtils/Rocket.Chat
[]
['README.md']
------------------ Rocket.Chat
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Mysql
[]
['README.md']
------------------ Mysql
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Site
['license', 'css', 'js', 'img', 'mysql-README', 'fonts', 'bash-README']
['index.html', '404.html']
------------------ Site
--------------------- index.html
--------------------- 404.html
/Users/rlaney/.cheat/NEW/MayccollUtils/Site/license
['highlight.js']
[]
--------------------- license
/Users/rlaney/.cheat/NEW/MayccollUtils/Site/license/highlight.js
[]
['LICENSE']
------------------------ highlight.js
--------------------------- LICENSE
/Users/rlaney/.cheat/NEW/MayccollUtils/Site/css
[]
['bootstrap-custom.min.css', 'highlight.css', 'prettify-1.0.css', 'font-awesome-4.0.3.css', 'base.css']
--------------------- css
------------------------ bootstrap-custom.min.css
------------------------ highlight.css
------------------------ prettify-1.0.css
------------------------ font-awesome-4.0.3.css
------------------------ base.css
/Users/rlaney/.cheat/NEW/MayccollUtils/Site/js
[]
['highlight.pack.js', 'prettify-1.0.min.js', 'base.js', 'bootstrap-3.0.3.min.js']
--------------------- js
------------------------ highlight.pack.js
------------------------ prettify-1.0.min.js
------------------------ base.js
------------------------ bootstrap-3.0.3.min.js
/Users/rlaney/.cheat/NEW/MayccollUtils/Site/img
[]
['favicon.ico', 'grid.png']
--------------------- img
------------------------ favicon.ico
------------------------ grid.png
/Users/rlaney/.cheat/NEW/MayccollUtils/Site/mysql-README
[]
['index.html']
--------------------- mysql-README
------------------------ index.html
/Users/rlaney/.cheat/NEW/MayccollUtils/Site/fonts
[]
['fontawesome-webfont.svg', 'fontawesome-webfont.ttf', 'fontawesome-webfont.woff', 'fontawesome-webfont.eot']
--------------------- fonts
------------------------ fontawesome-webfont.svg
------------------------ fontawesome-webfont.ttf
------------------------ fontawesome-webfont.woff
------------------------ fontawesome-webfont.eot
/Users/rlaney/.cheat/NEW/MayccollUtils/Site/bash-README
[]
['index.html']
--------------------- bash-README
------------------------ index.html
/Users/rlaney/.cheat/NEW/MayccollUtils/Localhost
[]
['index.php']
------------------ Localhost
--------------------- index.php
/Users/rlaney/.cheat/NEW/MayccollUtils/Synergy
[]
['README.md']
------------------ Synergy
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Javascript
[]
['README.md']
------------------ Javascript
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Puppet
[]
['README.md']
------------------ Puppet
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Brimir
[]
['README.md']
------------------ Brimir
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Ruby
[]
['README.md']
------------------ Ruby
--------------------- README.md
/Users/rlaney/.cheat/NEW/MayccollUtils/Remote
[]
['README.md']
------------------ Remote
--------------------- README.md
'''
