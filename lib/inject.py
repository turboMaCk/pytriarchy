# This will inject the logic to override imports

def self_inject():
    import inspect
    import sys

    self = sys.modules[__name__]
    imported = [ (name, obj) for name, obj in inspect.getmembers(self) if inspect.ismodule(obj) ]
    for name, obj in imported:
        if name == 'os':
            globals()['os'] = __import__('patched_os')

self_inject()
# Module code itself will follow

