# Tar VS Wheel
Source - stack overflow

This answered it for me (directly from the wheel PEP):

```
Python needs a package format that is easier to install than sdist.
Python's sdist packages are defined by and require the distutils 
and setuptools build systems, running arbitrary code to build and
install, and re-compile, code just so it can be installed into a 
new virtualenv. This system of conflating build-install is slow,
hard to maintain, and hinders innovation in both build systems and 
installers.

Wheel attempts to remedy these problems by providing a simpler interface between 
the build system and the installer. The wheel binary package format 
frees installers from having to know about the build system, saves 
time by amortizing compile time over many installations, and removes the 
need to install a build system in the target environment.
```

https://www.python.org/dev/peps/pep-0427/#rationale

Note the tarballs we're speaking of are what are referred to as "sdists" above.

