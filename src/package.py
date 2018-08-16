"""

File:           package.py 
Author:         Josh Kaplan
Description:    Defines a package.

"""

from .element import Element

class Package(Element):
    
    def __init__(self, name=None, parent=None):
        super(Package, self).__init__(name=name, parent=parent)
        self._contains = []
