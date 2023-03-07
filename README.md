# Pytriarchy

Pytriarchy demonstrates how to dynamic nature of the python3 language to deny access to certain functions to
given module. Because girls can't be astronauts.

This code is dedicated to [Valentina Tereshkova](https://en.wikipedia.org/wiki/Valentina_Tereshkova)

## Disclaimer(s)

> Use of this code might cause brain cancer.

1. Author of this package doesn't in endorse "pytriarchy" or any believe systems that might accidentally rhyme with it.
2. Author of this package doesn't endorse [United Russia](https://en.wikipedia.org/wiki/United_Russia)
3. Author of this package is most definitely NOT an expert python programmer. This code is for education purposes only.
4. Implementation provided in this repository is [INCOMPLETE](#Limitations) proof of concept

__This implementation is not meant for adding real security guarantees. If you're looking for restricting python3 process
you should use proper virtualization technique or apis provided for this purpose by your OS (eg. [cgroups](https://www.man7.org/linux/man-pages/man7/cgroups.7.html) or [namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html))__

## What This Does

Code in this repository leverages dynamic nature of Python3 programming language and runtime and uses runtime inspection
to deny accessibility to certain functions from certain modules.
This might be potentially useful to restricting some functionally only from some of the modules in python process
while allowing others to access those.

This works roughly as following:

1. Supply patched version of module in question like [`patched_os.py`](patched_os.py)
2. Leverage [`lib.patch_in`](lib/patch_in.py) to supply on non overridden functions into the module.
3. Inject [`lib.inject](lib/inject.py) to the module to patch its imports

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

Example file [`file.py`](file.py) ran through [`python3`](python3) shell script that injects the file:

```
./python3 file.py
file.py
you cannot
=> will evaluate:
=> b'b3MuZ2V0bG9naW4oKQ=='
you cannot
But I can get PATH from env /usr/local/...
But other modules can! marek
```

## LICENSE

[LICENSE](LICENSE)
