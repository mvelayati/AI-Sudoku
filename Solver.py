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
        timelimit = self.time + 300
        self.num_backtracks = 0

        self.solution.push(copy(Sudoku))

        is_solved = solve_recurse(level, order_method, timelimit)

        return [is_solved, self.num_backtracks, time.process_time() - self.time, self.solution.front()]

    def solve_recurse(level, order_method, timelimit):
        Sudoku = copy(self.solution.front())
        is_solved = Sudoku.is_solved() # Check if already solution

        while(not is_solved and time.process_time() < timelimit):

            spot = order_method(Sudoku) # choose which spot to assign

            for possibility in spot.domain():
                Sudoku.assign(spot, possibility)

                if Sudoku.forward_prop(level, spot):
                    # save a copy of puzzle each time assignment isn't illegal
                    self.solution.push(copy(Sudoku))

                    # move to the next assignment
                    if solve_recurse(level, order_method, timelimit):
                        # there's a solution below!
                        return True
                    else:
                        # this assignment did not lead to a solution
                        self.solution.pop()

                # made to the end of this for loop; you are backtracking
                self.num_backtracks += 1 # continue searching possibilities for valid propogations
                Sudoku = copy(self.solution.front()) # reset the puzzle to last partial solution

        return is_solved
