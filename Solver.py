#!/usr/bin/python3

import copy, time
from Sudoku import Sudoku

class Solver(object):
    """docstring for Solver. The Solver object solves Sudoku puzzles using a tunable level of complexity."""
    def __init__(self):
        self.num_backtracks = 0 # The number of times the solver needed to undo a value assignment
        self.board = None # holds the game board
        self.solution = [] # list that holds snap shots of the game each time a value is assigned
        self.time = float('inf'); # The total amount of time it takes to solve a problem

    """Method that attempts to solve the Sudoku puzzle with given level of complexity and order method. It returns a list [is_solved, num_backtracks, run_time].
    #order_method is a function that returns which spot should be tried next for assignment
    #level is a value in the range [0,4) that determines the complexity of the sovler.
    #Sudoku is a Sudoku object. The starting state of the puzzle."""
    def solve(Sudoku, level, order_method):
        self.time = time.process_time()
        is_solved = False
        self.num_backtracks = 0

        # Do some things here

        return [is_solved, self.num_backtracks, time.process_time() - self.time]
