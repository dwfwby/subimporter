from importlib.machinery import SourceFileLoader
import os.path

def subimport(name):
    path = f"{name}/__init__.py"
    if(os.path.exists(path)):
        return SourceFileLoader(name, path).load_module()