#!/usr/bin/env python 
"""

File:           __main__.py 
Author:         Josh Kaplan
Description:    Creates some models.

"""

import argparse
import os
import random
import time

from .element import Element
from .model import Model
from .package import Package
from .block import Block
from .link import Link

wordsfile = '{}/../data/wordlist_1000.txt'.format(os.path.dirname(__file__))
wordlist = open(wordsfile).read().splitlines()
used = []
elements = []

def main():
    # CLI
    parser = argparse.ArgumentParser()
    parser.add_argument('height', type=int, help='Model tree height')
    parser.add_argument('width', type=int, help='Model tree width')
    args = parser.parse_args()
    
    start = time.time()
    model = generate_model(args.height, args.width)
    elapsed = time.time() - start
    print_model(model)
    print 'Created {:d} elements in {:.3f} ms.'.format(len(elements), elapsed)


def get_name():
    name = ' '.join([random.choice(wordlist), random.choice(wordlist)])
    while name in used:
        name = ' '.join([random.choice(wordlist), random.choice(wordlist)])
    used.append(name)
    return name
    

def generate_model(height, width):
    assert height >= 1 
    assert width >= 1
    return generate_model_helper(height, width, depth=0, parent=None)
    
    
def generate_model_helper(height, width, depth=0, parent=None):
    # If at the start, create a top level model
    if depth == 0:    
        parent = Model(name=get_name())
        elements.append(parent)
        return generate_model_helper(height, width, depth=depth+1, parent=parent)
    
    if depth < height: 
        for i in range(width):
            T = random.choice(['Package', 'Block', 'Link'])
            if T == 'Package':
                p = Package(name=get_name(), parent=parent)
                elements.append(p)
                generate_model_helper(height, width, depth=depth+1, parent=p)
            elif T == 'Block':
                b = Block(name=get_name(), parent=parent)
                elements.append(b)
            elif T == 'Link':
                l = Link(name=get_name(), parent=parent, 
                            source=random.choice(elements), 
                            target=random.choice(elements))
    
    
    # Once we've reached out targeted height, return
    return parent


def print_model(e, depth=0):
    string = '%s%s (%s) %s' % ('  '*depth, e.id, e.__class__.__name__, e._name)
    if e.__class__.__name__ == 'Link':
        string += ' [%s -> %s]' % (e._source._name, e._target._name)
    
    print string
    
    if e.__class__.__name__ in ['Model', 'Package']:
        for c in e._contains:
            print_model(c, depth+1)


# Call main
if __name__ == '__main__':
    main();
