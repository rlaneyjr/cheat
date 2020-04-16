# defaults -- access the Mac OS X user defaults system
# defaults _[-currentHost | -host hostname]_ **commands**

## Commands:
**read**
_Prints all of the user's defaults, for every domain, to standard output_

**read domain**
_Prints all of the user's defaults for domain to standard output_

**read domain key**
_Prints the value for the default of domain identified by key_

**read-type domain key**
_Prints the plist type for the given domain identified by key_

**write domain key 'value'**
_Writes value as the value for key in domain_
# value must be a property list, and must be enclosed in single quotes.
defaults write com.companyname.appname "Default Color" '(255, 0, 0)'

**write domain 'plist'**
_Overwrites the defaults information in domain with that given as plist_
# plist must be a property list representation of a dictionary,
# and must be enclosed in single quotes.
# erases any previous defaults for com.companyname.appname and
# writes the values for the two names into the defaults system.
defaults write com.companyname.appname '{ "Default Color" = (255, 0, 0);
                                          "Default Font" = Helvetica; }';

**delete domain**
_Removes all default information for domain_

**delete domain key**
_Removes the default named key from domain_

**domains**
_Prints the names of all domains in the user's defaults system_

**find word**
_Searches for word in the domain names, keys, and values of the user's defaults,
and prints out a list of matches_

**help**
_Prints a list of possible command formats_

# Specifying domains:

**domain**
_If no flag is specified, domain is a domain name of the form
com.companyname.appname_
defaults read com.apple.TextEdit

**-app application**
_The name of an application may be provided instead of a domain
using the -app flag_
defaults read -app TextEdit

**filepath**
_Domains may also be specified as a path to an arbitrary plist
file, with or without the '.plist' extension_
defaults read ~/Library/Containers/com.apple.TextEdit/Data/Library/Preferences/com.apple.TextEdit.plist

# will write the key 'foo' with the value 'bar' into the plist
defaults write ~/Desktop/TestFile foo bar
