# Join PDF Files into a new file
To do this you need to install the ghostscript package
(it doesn't necessarilly come bundled with imagemagic).

Ghostscript is a scripting language used to interact with the
`postscript` and `pdf` formats.

``` sh
convert -density 220 file1.pdf file2.pdf ... output.pdf
```

