# rrt_helper_functions
#
# A set of functions to make coding RRT and its variants a little
# easier. Utilizes this assignment set's world class and a whole
# bunch of tuples.
#
# Author:
#   Travis Hainsworth
#   CSCI 3022 - Introduction to Robotics
#   CU Boulder
#   Fall 2024
from math import dist


# --------------- L2 Norm (euclidean distance) ---------------- #
# returns an int
def L1_norm(position_1: tuple, position_2: tuple):
    x = abs( position_1[0] - position_2[0] )
    y = abs( position_1[1] - position_2[1] )
    return int(x+y)
# ------------------------------------------------------------- #


# --------------- L2 Norm (euclidean distance) ---------------- #
# returns a float
def L2_norm(point_1: tuple, point_2: tuple):
    return dist(point_1, point_2)
# ------------------------------------------------------------- #



# ------------------------ Unit Vector ------------------------ #
# returns a tuple of 2 floats
def unit_vector_between_2_points(point_1: tuple, point_2: tuple):
    norm = L2_norm(point_1, point_2)
    
    # Working with tuples isn't very straight forward, so I'll pull 
    # out each element
    delta_x = point_2[0] - point_1[0]
    delta_y = point_2[1] - point_1[1]

    return (delta_x/norm, delta_y/norm)
# ------------------------------------------------------------- #



# ----------------------- Get New Point ----------------------- #
# Based on the point of the closest node and the direction where
# the new node should be, return the point where the new node
# should be
#
# returns a tuple of ints
def get_new_point(current_point: tuple, unit_vector: tuple, step_magnitude: int, world_size: tuple):
    x_current, y_current = current_point
    
    delta_x = unit_vector[0] * step_magnitude
    delta_y = unit_vector[1] * step_magnitude

    # Find new point rounded down
    x_new = int(x_current + delta_x)
    y_new = int(y_current + delta_y)

    # See if new point is actually in the world
    if x_new < 0: 
        x_new = 0
    elif x_new >= world_size[0]: 
        x_new = world_size[0] - 1

    if y_new < 0:
        y_new = 0
    elif y_new >= world_size[1]:
        y_new = world_size[1] - 1

    return (x_new, y_new)
# ------------------------------------------------------------- #



# --------------------- Crosses Obstacle ---------------------- #
# Identify if a straight line between two points would cross any
# of the world's obstacles
#
# Returns a boolean if an obstacle would be crossed
def crosses_obstacle(point_1: tuple, point_2: tuple, world):
    # I'll begin by pulling out coordinates in an effort to make 
    # things more readable
    #
    # Mathematically the order of the points doesn't matter, but for
    # generating lists it does because we'll be using range(x1, x2)
    if point_2[0] > point_1[0]:
        x1, y1 = point_1
        x2, y2 = point_2
    else:
        x1, y1 = point_2
        x2, y2 = point_1

    # Slope is rise/run, if the line is vertical then we have problems
    rise = float(y2 - y1)
    run = float(x2 - x1)

    # As long as the line isn't vertical:
    if run != 0:
        slope = rise/run
        intercept = float(y1) - slope*float(x1)

        line = lambda x : slope*float(x) + intercept

        # We'll round down the y coordinates via int() to find the nearest node
        list_o_coordinates = [(x, int(line(x))) for x in range(x1, x2+1)] # Including +2 so that we check that the point isn't a wall either
    # For vertical lines
    else:
        list_o_coordinates = [(x, y1) for x in range(x1, x2+1)]

    if any(item in world.wall_list for item in list_o_coordinates):
        # print("here")
        return True
    return False
    # See if any of these intermediate nodes are a wall
    # for row, col in list_o_coordinates:
    #     if world.grid[row][col].wall:
    #         print("here 1")
    #         return True
    #     if world.grid[row][col+1].wall:
    #         print("here 2")
    #         return True
    # return False
# ------------------------------------------------------------- #
