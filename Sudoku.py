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
            tuples(3,start.row())
            tuples(3,start.row())
        if k >= 2:
            tuples(2,start.row())
            tuples(3,start.row())
        if k >= 1:
            for spot in start.neighborhood():
                if not spot.is_assigned():
                    domain = 0
                    for r in spot.row():
                        domain = domain | r.domain
                    domain = (~domain & spot.domain)
                    if bin(domain).count('1') == 1
                        assign(spot, domain)
                if not spot.is_assigned():
                    domain = 0
                    for c in spot.col():
                        domain = domain | c.domain
                    domain = (~domain & spot.domain)
                    if bin(domain).count('1') == 1
                        assign(spot, domain)
                if not spot.is_assigned():
                    domain = 0
                    for b in spot.box():
                        domain = domain | b.domain
                    domain = (~domain & spot.domain)
                    if bin(domain).count('1') == 1
                        assign(spot, domain)

        if k >= 0:
            for spot in start.neighborhood():
                if not spot.is_assigned() and spot.domain_size() == 1:
                    self.assign(spot,spot.domain)
                    forward_prop(k, spot)

        return is_valid
    def tuples(k,set)
        maybe_matches = []
        for spot in set:
            # find all domains size 2
            bin(spot.domain).count('1') == k
            maybe_matches.append(spot)

        # see if there are any pairs among the domains
        while len(maybe_matches) > 1:
            matches = [0]
            for i = 1:len(maybe_matches):
                if maybe_matches[0].domain == maybe_matches[i].domain:
                    matches.append(i)
            if len(matches) == k:
                #remove the domains of these k from their neighborhoods
                allneighborsdomains & ~thesematchesdomains

        for spot in start.col():

        for spot in start.box():
