this file --
echo $(( $(( $( date +%s ) - $( date -d "1989-11-29" +%s ) )) / 86400 )) # Calculate how many days old you are. Uses GNU syntax.
