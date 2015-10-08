#!/bin/bash -x
# this file -- enos.in/cd -- https://raw.githubusercontent.com/soneups/scratchcode/master/cd.sh
echo $(( $(( $( date +%s ) - $( date -d "1989-11-29" +%s ) )) / 86400 )) # Calculate how many days old you are. Uses GNU syntax.
