# Pytriarchy

Pytriarchy demonstrates how to leverage dynamic nature of the python3 language to deny access
to certain functions to given module.
Because girls can't be astronauts.

This code is dedicated to [Valentina Tereshkova](https://en.wikipedia.org/wiki/Valentina_Tereshkova)

## Disclaimer(s)

> Use of this code might cause brain cancer.

1. Author of this package doesn't endorse "pytriarchy" or any believe systems that might accidentally rhyme with it.
2. Author of this package doesn't endorse [United Russia](https://en.wikipedia.org/wiki/United_Russia)
3. Author of this package is most definitely NOT an expert python programmer. This code is for education purposes only.
4. Implementation provided in this repository is [INCOMPLETE](#Limitations) proof of concept

__This implementation is not meant for adding real security guarantees. If you're looking for restricting python3 process
you should use proper virtualization technique or apis provided for this purpose by your OS (eg. [cgroups](https://www.man7.org/linux/man-pages/man7/cgroups.7.html) or [namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html))__

## What This Does

Code in this repository leverages dynamic nature of Python3 programming language and runtime and uses runtime inspection
to deny access to certain functions to certain modules.
This might be potentially useful for restricting some functionally only to some of the modules in python process
while allowing others to use those.

This works roughly as following:

1. Supply patched version of module in question like [`patched_os.py`](patched_os.py)
2. Leverage [`lib.patch_in`](lib/patch_in.py) to forward all non overridden functions to the original module
3. Inject [`lib.inject`](lib/inject.py) to the module to patch its imports

## Demo

Example file [`file.py`](file.py) ran normally with python:

```
python3 file.py
marek
=> will evaluate:
=> b'b3MuZ2V0bG9naW4oKQ=='
marek
But I can get PATH from env /usr/local/...
Not defined
```

Example file [`file.py`](file.py) ran through [`python3`](python3) shell script that injects the pytriarchy:

```
./python3 file.py
you cannot
=> will evaluate:
=> b'b3MuZ2V0bG9naW4oKQ=='
you cannot
But I can get PATH from env /usr/local/...
But other modules can! marek
```

## Limitations

This implementations so far covers only top level module imports.
It was only tested with basic code example provided in the repository.
Most likely there are ways around the restrictions imposed by the inject logic
like:

```python
def foo():
    import os
    os.
```

and similar.

This library also at the moment doesn't resolve module aliasing so for instance:

```python
import os as its_mine_os

its_mine_os.getlogin()
```

would require change in patching logic.

Lastly the [shell script](python3) is performing
reordering of imports in the file being loaded.
This might lead to issues in cases like

```python
import foo as a
# use a
a.foo()

import bar as a
# use a again
a.bar()
```

in general a pretty tricky part of this approach is to find a right time when
to run the patching logic. It has to be before any code that should be patched
is executed but after all the modules are imported.

## LICENSE

[LICENSE](LICENSE)
