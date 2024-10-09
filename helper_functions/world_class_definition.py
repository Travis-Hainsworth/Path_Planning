# Definition of a class representing the world
#
# This object contains all of the nodes in the path planning graph
#
# The world class has the following info:
#   grid        - a 2d list of the nodes arranged by [row][column]
#   start       - a tuple of the starting (row, column)
#   goal        - a tuple of the goal (row, column)
#   action_cost - an int representing how much it costs to take an action
#
# There is also info that you shouldn't need to use or worry about:
#   pixel dimensions - calculated based on the world's grid size and the size of the screen
#
#   There are also two function:
#       compile_neighbors - adds the neighbors of each node to the node's neighbors list
#       add_wall - modifies the node's wall boolean and also updates the pygame screen
#
# Author:
#   Travis Hainsworth
#   CSCI 3022 - Introduction to Robotics
#   CU Boulder
#   Fall 2024
import pygame
from helper_functions.node_class_definition import *

class world_class:
    def __init__(self, world_height, world_width, start_location, goal_location, screen_size):
        # Create the list of lists that holds the nodes
        self.grid = [[node_class(i,j) for j in range(world_width)] for i in range(world_height)]

        # Save the start and goal locations, as well as how much it costs to take an action
        self.start = start_location
        self.goal = goal_location
        self.action_cost = 1

        # Define the start's cost as zero
        self.grid[self.start[0]][self.start[1]].true_cost = 0

        # This flattened_grid is convenient to have if you are going to be making dictionaries 
        # in the future
        self.flattened_grid = [node for row in self.grid for node in row]

        # Save the world and pixel dimensions
        self.world_height = world_height
        self.world_width = world_width
        self.world_size = (world_height, world_width)


        self.pixel_height = screen_size[0]//world_height
        self.pixel_width = screen_size[1]//world_width

        # Store a list of wall locations. This is redundant info shared with each node's wall boolean
        # However, it is nice to have a concise list of walls for various checks that doesn't
        # require analyzing each node
        self.wall_list = []

    # Here we will fill in the node's list of neighbors based on the neighbors touching each node
    def compile_neighbors(self):
        for row in self.grid:
            for node in row:
                node_row, node_col = node.position

                # Up action
                if node_row != 0:
                    neighbor = self.grid[node_row-1][node_col]
                    if not neighbor.wall:
                        node.neighbors.append(neighbor)
                # Down action
                if node_row != self.world_height-1:
                    neighbor = self.grid[node_row+1][node_col]
                    if not neighbor.wall:
                        node.neighbors.append(neighbor)
                # Right action
                if node_col != 0:
                    neighbor = self.grid[node_row][node_col-1]
                    if not neighbor.wall:
                        node.neighbors.append(neighbor)
                # Left action
                if node_col != self.world_width-1:
                    neighbor = self.grid[node_row][node_col+1]
                    if not neighbor.wall:
                        node.neighbors.append(neighbor)
                
    # This is used for dynamically adding walls to the world in the interactive map
    def add_wall(self, screen):
        wall_color = (0, 0, 0)
        mouse_location = pygame.mouse.get_pos()
        node_col = mouse_location[0]//self.pixel_height
        node_row = mouse_location[1]//self.pixel_width
        pygame.draw.rect(screen, wall_color, (node_col*self.pixel_width, node_row*self.pixel_height, self.pixel_width, self.pixel_height))
        pygame.display.flip()
        self.grid[node_row][node_col].wall = True
        self.wall_list.append((node_row, node_col))