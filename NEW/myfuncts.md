# Copy man page to a cheat
m2c example

# Copy the output to a cheat
cat example | 2cheat

# Call map custom function
ipy_call_map

# Simple calculator
calc

# Create a new directory and enter it
mkd mydir

# Change working directory to the top-most Finder window location
cdf

# Create a .tar.gz archive, using `zopfli`, `pigz` or `gzip` for compression
targz my-file1 my-file2

# Determine size of a file or total size of a directory
fs
fs my-file.wtf

# Create a data URL from a file
dataurl my-file.wtf

# Create a git.io short URL. Usage: gitio `slug` `url`
gitio 'example' 'example.com'

# Start an HTTP server from a directory, optionally specifying the port
server
server 8000

# Start a PHP server from a directory, optionally specifying the port (Requires PHP 5.4.0+.)
phpserver
phpserver 8080

# Compare original and gzipped file size
gz example.gz

# Syntax-highlight JSON strings or files
json_hi example.json
json_hi '{"foo":42}'
echo '{"foo":42}' | json_hi

# Run `dig` and display the most useful info
digga 'cisco.com'

# UTF-8-encode a string of Unicode symbols
escape "₪ & ฿ ® φ"

# Decode \x{ABCD}-style Unicode escape sequences
unidecode '\u00A9'
unidecode '\u03B1'

# Get a character’s Unicode code point
codepoint 'Ω'

# Show all the names (CNs and SANs) listed in the SSL certificate
# for a given domain
getcertnames 'example-ssl.crt'

# `s` with no arguments opens the current directory in Sublime Text.
s

# `a` with no arguments opens the current directory in Atom Editor.
a

# `c` with no arguments opens the current directory in VScode Editor.
c

# `m` with no arguments opens the current directory in mVim.
m

# `v` with no arguments opens the current directory in Vim.
v

# `o` with no arguments opens the current directory.
o

# `tre` is a shorthand for `tree` with hidden files and color enabled, ignoring
# the `.git` directory, listing directories first. The output gets piped into
# `less` with options to preserve color and line numbers, unless the output is
# small enough for one screen.
tre
