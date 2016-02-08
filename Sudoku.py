#!/usr/bin/python3

class Sudoku(object):
    """docstring for """
    def __init__(self, arg):
        self.arg = arg

    '''Propogates constrains forward from start. Returns true of propogation did not result any empty domains.
    #k is the complexity level of the forward propogation. For k = n, forward_prop will execute levels <= n.
    k = {
    0: checks for spots that have a domain of size 1;
    1: checks for values whose neighbor's domains are missing exactly one value;
    2: checks neighborhoods for pairs of spots with the exact same domain of size 2;
    3: checks neighborhoods for triples of spots with the exact same domain of size 3}'''
    def forward_prop(k, start):
        is_valid = True

        if k >= 3:
            None # do something
        if k >= 2:
            None # do something
        if k >= 1:
            None # do something
        if k >= 0:
            None # do something

        return is_valid
