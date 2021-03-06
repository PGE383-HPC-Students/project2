#!/usr/bin/env python

import os, sys
import numpy as np

from laplace import LaplaceSolver


class LaplaceSolverMPI(LaplaceSolver):
    
    def __init__(self, comm, **kwargs):
        self.comm = comm
        self.rank = comm.rank
        self.size = comm.size
        super().__init__(**kwargs)
            
        
    def set_boundary_condition(self, **kwargs):
        if self.rank == 0:
            super().set_boundary_condition(**kwargs)
        
        
    def solve(self, max_iterations=10000, tolerence=1.0e-16, verbose=False):

        #####################
        ### Add code here ###
        #####################

        return
        


    def get_solution(self):

        #####################
        ### Add code here ###
        #####################

        return
            

if __name__ == "__main__":
    
    from mpi4py import MPI
    
    comm = MPI.COMM_WORLD

    solver = LaplaceSolverMPI(comm, nx=40, ny=30)
    solver.set_boundary_condition(side='right', boundary_condition_function=lambda x,y: 5)
    solver.set_boundary_condition(side='left', boundary_condition_function=lambda x,y: 5)
    # solver.solve(verbose=True)
    # u = solver.get_solution()
    # if comm.rank == 0:
    #     print(u)
