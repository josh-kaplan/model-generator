"""

File:           link.py 
Author:         Josh Kaplan
Description:    Defines a link.

"""

from .element import Element

class Link(Element):
    
    def __init__(self, name=None, parent=None, source=None, target=None):
        super(Link, self).__init__(name=name, parent=parent)
        self._source = source
        self._target = target
