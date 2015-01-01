#!/usr/local/bin/python3
import sys

if len(sys.argv) <  2:
    print("USAGE: alias_finder <shell config file>")
    exit(0)

filename = sys.argv[1]

output_file = ".aliases"
aliases = []
#Open the given config_file
with open(filename, 'r') as config_file:
    #Go through each line
    for line in config_file:
        #If the line is an alias, add it to the array
        if "alias" in line:
            aliases.append(line)
#Write the found aliases to an output file
with open(output_file, 'w') as output:
    for alias in aliases:
        output.write(alias)
#Tell the user how many aliases were found
print("Wrote " + str(len(aliases)) + " aliases")
