"""

File:           element.py 
Author:         Josh Kaplan
Description:    Defines an element.

"""

import time
import uuid


class Element(object):
    
    def __init__(self, name=None, parent=None):
        self._id = uuid.uuid4() 
        self._created = time.time()
        self._updated = time.time()
        self._name = name
        
        self._parent = parent
        if parent is not None:
            assert parent.__class__.__name__ in ['Model', 'Package']
            self._parent = parent
            parent._contains.append(self)
                
    @property
    def id(self):
        return str(self._id)
    
    @id.setter
    def id(self, x):
        pass
