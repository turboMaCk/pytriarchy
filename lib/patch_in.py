import sys
import inspect

# Patch in all allowed functions
def patch_in(self_name, mod_name):
    # inject the original module
    real_module = __import__(mod_name)
    delegate_to = [ (name, obj) for name, obj in inspect.getmembers(real_module) if inspect.isfunction(obj) ]

    # collect overrides
    self = sys.modules[self_name]
    defined_names = set([ name for name, obj in inspect.getmembers(self) if inspect.isfunction(obj) ])

    # patch
    for name, obj in delegate_to:
        if not (name in defined_names):
            # self[name] = obj
            setattr(self, name, obj)
            # self.__setattr__(name, real_module[name])
