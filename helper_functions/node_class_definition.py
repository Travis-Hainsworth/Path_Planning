# Definition of a node
#
# Used to represent a node/vertex in a path planning graph.
#
# The node has the following info:
#   position   - a tuple, row and column where the node is located 
#   neighbors  - a list of other neighboring nodes
#   previous   - the node that led the path to this node
#   true_cost  - the cost to get to this node from the starting node
#   total_cost - if applicable, the true_cost + estimated cost from a heuristic
#   wall       - boolean (True if this node is a wall, False if not)
#
# Note:
#   The neighbors will be automatically populated when the world is defined
#
# Author:
#   Travis Hainsworth
#   CSCI 3022 - Introduction to Robotics
#   CU Boulder
#   Fall 2024

class node_class:
    def __init__(self, node_row, node_col):
        self.position = (node_row, node_col)
        self.neighbors = []
        self.previous = None
        self.wall = False
        self.true_cost = float('inf')
        self.total_cost = float('inf')