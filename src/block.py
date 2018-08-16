"""

File:           block.py 
Author:         Josh Kaplan
Description:    Defines a block.

"""

from .element import Element

class Block(Element):
    
    def __init__(self, name=None, parent=None):
        super(Block, self).__init__(name=name, parent=parent)
