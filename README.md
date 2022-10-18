# mda_xdrlib

A stand-alone XDRLIB module extracted from cpython 3.10.8


## Why does this package exist?

The xdrlib package has historically been a feature of the core python library.
However, as of Python 3.11, the module was deemed to no longer be widely used
and has been deprecated, with a target removal version of Python 3.13.

Several of the MDAnalysis projects rely on the xdrlib module for their
functionality, specifically for parsing GROMACS TPR and EDR files. To
avoid a need to vendor in the xdrlib functionality in multiple projects,
we take the approach of creating this stand-alone module which contains
the python 3.10.8 xdrlib code and its relevant tests.


## Changes from the cpython implementation

The majority of this code is copied from the 3.10.8 release of cpython.
Any modifications of the code are mostly cosmetic. A full copy of these
modifications can found in the [CHANGES](./CHANGES) file.


## License

Being taken from the cpython 3.10.8 release, the code within this repository
falls under the Python Software Foundation License Version 2. Any
documentation is also dual licensed with both the PSF License Version 2 and
the zero-clause BSD license. More information can be found in
the [LICENSE](./LICENSE) file.
