# Readme
## How to browse notes
Call `fzfp` then type keywords to find a note of interest.

## How to contribute?
Notes are organised by subjects, each subject being a directory.
Leave a note for a subject as text file in a subject directory.

## How to install fzfp?
First download `fzf` from github.

Then download `bat` from github or with the cargo package manager.

Then copy this function in your shell profile:
``` sh
### Fzf with preview mode
# $1 is the language parameter (-l) for bat
#
# dependencies: bat, fzf
fzfp() {
	if [ -n "$1" ]; then
		PLANG="-l $1"
	fi
	fzf --exact --preview="bat --color always $PLANG {}"
}
```
