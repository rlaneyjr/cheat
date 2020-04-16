# copy the active line from the command line buffer 
# onto the system clipboard (requires clipcopy plugin)
# Keymapping: `CTRL-O`
copybuffer

# Copies the pathname of the current directory to the system or X Windows clipboard
copydir

# Copies the contents of a given file to the system or X Windows clipboard
copyfile 'example-file.wtf'

# Change file extensions recursively in current directory
chgext 'man' 'md'

# Connect and authenticate to MongoDB "nmis" for Opmantek
# Arguments -> $1 The host where mongodb is running
opmon 'dc4-poller'

# Enter bash shell inside docker container
sdoc 'example-container'

# Enter zsh shell inside docker container
zdoc 'example-container'

# Load .env file into shell session for environment variables
envup

# Touch a file making a script header and executable
# Arguments -> $1 The file name
msh 'example.sh'

# File search & replace
ff 'mysearch'
fr 'mysearch' 'myreplace'

# Quick and colorful help
hlp 'ls'

# Copy gitignore file
cgi

# Make directory and change into it.
mcd

# Setup ssh for me
sshr

# `cpv` function for local copy `cp` and gives you the security of `rsync`
cpv 'example-dir' '/examples/example-dir'

# Deletes all file in the current working directory days old as a numeric arg
# Arguments -> $1 Number of days old
clrfiles 10

# prints an error message to STDERR
# Arguments: $@ -> message to print
perr "My error message"

# print a warning nessage to STDERR
# Arguments: $@ -> message to print
pwarn "My warning message"

# print a usage message and then exits
# Arguments: $@ -> message to print
puse "My usage message"

# ask a yes/no question
# Arguments: $1 -> The prompt
#            $2 -> The default answer (optional)
# Variables: yesno -> set to the user response (y for yes, n for no)
prompt_yn "Do you like Pearl Jam?"
prompt_yn "Do you like Pearl Jam?" yes

# ask a question
# Arguments: $1 -> The prompt
#            $2 -> The default answer (optional)
# Variables: response -> set to the user response
prompt_resp "What time is it?"
prompt_resp "What time is it?" "playtime"

# print a list of process id(s) matching $1
# Arguments: $1 -> the process name to search for
get_pid 'firefox'

# print the numeric user id
# Arguments: $1 -> the user name
get_uid 'rlaney'

# print an input string to lower case
# Arguments: $@ -> the string
to_lower "PLEASE DO NOT YELL AT ME!"

# print an input string to upper case
# Arguments: $@ -> the string
to_upper "please speak up!"

# convert the input files to lower case
# Arguments: $@ -> files to convert
file_to_lower "/example/HELLO.MD"

# convert the input files to upper case
# Arguments: $@ -> files to convert
file_to_upper "/example/hello.md"

# rename all the files with a new suffix
# Arguments: $1 -> the old suffix (for example html)
#            $2 -> the new suffix (for example xhtml)
ren_all_suf 'md' 'txt'

# rename all the files with a new prefix
# Arguments: $1 -> the old prefix
#            $2 -> the new prefix
ren_all_pref 'old' 'new'

# convert a list of dos formatted files to the POSIX format
# Arguments: $@ -> the list of files to convert
dos2posix 'file1'
dos2posix 'file1' 'file2'

# convert a list of dos formatted files to the POSIX format
# Arguments: $@ -> the list of files to convert
posix2dos 'file1'
posix2dos 'file1' 'file2'

# print the system's name
os_name

# print out the number of characters which exist in a file
# Arguments: $@ -> the files to count the chars of
chars 'file-example'

# insert quotes in the beggining and the end of each file's line
# Arguments: $1 -> the file of which the contents will be quoted
ins_quotes 'file-example'

# remove all the files of a specific type that exist in the current directory
# Arguments: $1 -> the string to search in the output of `file'
# NOTE: use with caution...
rm_all 'wildcard'

# make a file executable
# Arguments: $@ -> what to match
cx 'file'

# count lines
# Arguments: $@ -> what to match
cl 'file'

# sort files
# Arguments: $@ -> what to match
fsort 'wildcard'

# sort mixed (directories & files)
# Arguments: $@ -> what to match
dsort 'wildcard'
dsort 'dir'

# simple way to keep a backup of a file
# Arguments: $1 -> the file
bkup 'file'

# show a message near the mouse
# useful for things like ``./build ; msg "libc build"''
# Arguments: $1 -> the message
msg "I am right here!"

# print a specific line of a file
# Arguments: $1 -> the line number
#            $2 -> the file
pln '101' 'myfile.wtf'

# create a directory and enter it
# Arguments: $1 -> the directory name
mkcd 'mydir'

# list all the files that are newer than the given
# Arguments: $1 -> the file name
newer 'myfile'

# list all the files that are older than the given
# Arguments: $1 -> the file name
older 'myfile'

# detect double words (eg. "hello my   my friend")
# Arguments: $1 -> the file(s) to be checked
dword 'myfile'
dword 'myfile1' 'myfile2'

# count word frequencies
# Arguments: $1 -> the file(s) to use while counting
wfreq 'myfile'
wfreq 'myfile1' 'myfile2'

# get the numeric value of a month (eg. march = 3)
# Arguments: $1 -> the month's name
# Variables: nmonth -> set to the value of the month
n_month 'feb'

# /usr/bin/cal improved
# examples:
# shows the full current year:
cal y
# shows march of the current year
cal mar
# shows april-june of the current year (note the spaces)
cal apr - jun
