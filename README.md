This is a simple script written in python 3 for seperating aliases from a
.bashrc or similar shell config file into a seperate file called .aliases. It
does not make any changes to the given shell config file. This script was
written because I moved from bash to zsh and had hundreds of aliases in
my .bashrc file without any type of organization. By separating my aliases into
a sepearte file I can continue to use my existing aliases with my new shell with
minimal effort. 

To use the generated .aliases file add:
source .aliases
to your shell config file.

Script usage:
./alias_finder <shell config file>

Example:
./alias_finder ~/.bashrc
