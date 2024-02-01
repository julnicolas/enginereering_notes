# Heredoc syntax
A Heredocument is routine allowing to write a multiline file content in place in bash.

``` sh
cat << EOF > myfile
first line
second line
EOF
```
Note - EOF can be any token. Could be FinDeLigne or whatever the user wants to use.

Output:
``` sh
-> cat myfile
first line
second line
->
```
