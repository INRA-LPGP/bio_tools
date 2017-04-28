import pkgutil
import bio_tools.commons as commons

# Dynamically imports any submodule inside 'env'
__all__ = []

for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    exec('%s = module' % module_name)


def get_data():
    env = []
    for importer, modname, ispkg in pkgutil.iter_modules(__path__):
        module = __import__(modname, fromlist="dummy")
        env.append({commons.NAME: module.NAME,
                    commons.PATH: module.PATH,
                    commons.DESCRIPTION: module.DESCRIPTION,
                    commons.DEFAULTS: module.DEFAULTS})
    return env


def show():
    env = get_data()
    out = ''
    for i, e in enumerate(env):
        out += (e[commons.NAME] +
                ' (' +
                e[commons.DESCRIPTION] +
                ')')
        if i < len(env) - 1:
            out += ','
    return out
