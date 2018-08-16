"""

File:           model.py 
Author:         Josh Kaplan
Description:    Defines a model.

"""

from .package import Package

class Model(Package):
    
    def __init__(self, name=None, parent=None):
        super(Model, self).__init__(name=name, parent=None)
        self._contains = []
