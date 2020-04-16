#!/usr/bin/env bash

# Convert man to html
zcat /usr/share/man/man1/man.1.gz  | groff -mandoc -Thtml

