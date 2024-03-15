# Download File
``` sh
curl -O "http://path/to/foo.txt"
```
Downloads `foo.txt` to `pwd`

To give it another file name rather use
``` sh
curl -o bar.txt "http://path/to/foo.txt"
```
Then it downloads foo.txt but names it
bar.txt
