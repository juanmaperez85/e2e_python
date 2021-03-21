import os
import inspect
from django.conf import settings
from django.utils.importlib import import_module


def get_page_class(classname):
    classname = classname.replace(" ", "")

    def is_valid_class(clazz):
        return inspect.isclass(clazz) and clazz.__name__ == classname

    for app in settings.INSTALLED_APPS:
        try:
            mod = import_module(app)
        except ImportError:
            continue
        module_dir = os.path.join(os.path.dirname(mod.__file__), 'features', 'pages')
        if os.path.isdir(module_dir):
            modname = '%s.features.pages' % mod.__name__
            try:
                pages_mod = import_module(modname)
                classes = inspect.getmembers(pages_mod, is_valid_class)

                if classes:
                    return classes[0][1]
                else:
                    continue

            except ImportError:
                raise ImportError("Class '{0}' not found in '{1}' package.".format(classname, modname))






