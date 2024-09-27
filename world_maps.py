# Premade Maps
#
# There are five maps:
#   small_map_1 and small_map_2 
#       which each make a screen 600x600 and a world with 20x20 nodes
#
#   big_map_1 and big_map_2
#       which each make a screen 600x600 and a world with 20x20 nodes
#
#   interactive_map( world_size, screen_size)
#       This interactive map allows users to draw the walls on the screen, then press any key to initiate 
#       the path planning. The inputs are:
#           world_size  - a tuple with (world_height, world_width) number of nodes
#           screen_size - a tuple with (screen_heigh, screen_size), I think these are the number of pixels.
# NOTE:
#   In our algorithms everything has been defined as (row, column)
#
#   In computer vision the coordinate frame is most commonly
#   (x,y) with the origin in the upper left of the frame and
#   positive y is going down. But this has been taken into account
#   in the helper functions and you don't need to do any conversions.
#   All of your work should be in (row, column) reference frame.
#
# NOTE:
#   Future me should probably make this into a function instead of rewriting the same thing a bunch 
#   of times
#
# Author:
#   Travis Hainsworth
#   CSCI 3022 - Introduction to Robotics
#   CU Boulder
#   Fall 2024
from helper_functions.world_class_definition import *
from helper_functions.screen_helper_functions import *



#---------------------------------------------------------------------------------------------------------#
#----------------------------------------- Small World 1 -------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
def small_map_1():
    # -------------------------- Basic Game Properties -------------------------- #
    # --------------------------- Create the Screen ----------------------------- #

    # define size of the app screen
    screen_size = (window_height, window_width) = 600, 600

    # define the grid AKA world size AKA number of nodes
    world_size = (world_height, world_width) = 20, 20

    # In the grid's (row, column) format
    start_location = (0, 0)
    goal_location = (world_height//2, world_width//2)
    
    # ---------------------------- Create the World ----------------------------- #
    # this is a representation of the world. See world_definition.py for more info
    world = world_class(world_height, world_width, start_location, goal_location, screen_size)

    # --------------------------- Create the Screen ----------------------------- #
    # This comes from screen_helper_functions.py and uses pygame
    screen = make_screen(world, screen_size)

    
    # ---------------------------- Define the Walls ----------------------------- #
    wall_loc = [(4,i) for i in range(3,6)]
    for wall in wall_loc:
        pygame.draw.rect(screen, (0,0,0), (wall[1]*world.pixel_width, wall[0]*world.pixel_height, world.pixel_width, world.pixel_height))
        world.grid[wall[0]][wall[1]].wall = True
    pygame.display.flip()

    
    # --------------------- Compile Each Node's Neighbors ----------------------- #
    # Once again, see world_definition.py for more info
    world.compile_neighbors()

    return world, screen





#---------------------------------------------------------------------------------------------------------#
#----------------------------------------- Small World 2 -------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
def small_map_2():
    # -------------------------- Basic Game Properties -------------------------- #
    # --------------------------- Create the Screen ----------------------------- #

    # define size of the app screen
    screen_size = (window_height, window_width) = 600, 600

    # define the grid AKA world size AKA number of nodes
    world_size = (world_height, world_width) = 20, 20

    # In the grid's (row, column) format
    start_location = (0, 0)
    goal_location = (world_height//2, world_width//2)
    
    # ---------------------------- Create the World ----------------------------- #
    # this is a representation of the world. See world_definition.py for more info
    world = world_class(world_height, world_width, start_location, goal_location, screen_size)

    # --------------------------- Create the Screen ----------------------------- #
    # This comes from screen_helper_functions.py and uses pygame
    screen = make_screen(world, screen_size)

    
    # ---------------------------- Define the Walls ----------------------------- #
    wall_loc_1 = [(6,i) for i in range(6,16)]
    wall_loc_2 = [(i,6) for i in range(6,16)]
    wall_loc = wall_loc_1 + wall_loc_2
    for wall in wall_loc:
        pygame.draw.rect(screen, (0,0,0), (wall[1]*world.pixel_width, wall[0]*world.pixel_height, world.pixel_width, world.pixel_height))
        world.grid[wall[0]][wall[1]].wall = True
    pygame.display.flip()

    
    # --------------------- Compile Each Node's Neighbors ----------------------- #
    # Once again, see world_definition.py for more info
    world.compile_neighbors()

    return world, screen





#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ Big World 1 --------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
def big_map_1():
    # -------------------------- Basic Game Properties -------------------------- #
    # --------------------------- Create the Screen ----------------------------- #

    # define size of the app screen
    screen_size = (window_height, window_width) = 800, 800

    # define the grid AKA world size AKA number of nodes
    world_size = (world_height, world_width) = 200, 200

    # In the grid's (row, column) format
    start_location = (0, 0)
    goal_location = (world_height//2, world_width//2)
    
    # ---------------------------- Create the World ----------------------------- #
    # this is a representation of the world. See world_definition.py for more info
    world = world_class(world_height, world_width, start_location, goal_location, screen_size)

    # --------------------------- Create the Screen ----------------------------- #
    # This comes from screen_helper_functions.py and uses pygame
    screen = make_screen(world, screen_size)

    
    # ---------------------------- Define the Walls ----------------------------- #
    wall_loc_1 = [(i,80) for i in range(80,120)]
    wall_loc_2 = [(i,120) for i in range(80,120)]
    wall_loc_3 = [(80,i) for i in range(80,120)]
    wall_loc_4 = [(120,i) for i in range(80,90)]
    wall_loc_5 = [(120,i) for i in range(110,121)]
    wall_loc = wall_loc_1 + wall_loc_2 + wall_loc_3 + wall_loc_4 + wall_loc_5
    for wall in wall_loc:
        pygame.draw.rect(screen, (0,0,0), (wall[1]*world.pixel_width, wall[0]*world.pixel_height, world.pixel_width, world.pixel_height))
        world.grid[wall[0]][wall[1]].wall = True
    pygame.display.flip()

    
    # --------------------- Compile Each Node's Neighbors ----------------------- #
    # Once again, see world_definition.py for more info
    world.compile_neighbors()

    return world, screen





#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ Big World 2 --------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
# This world has one big wall down the center with a gap bisecting the wall. The user inputs the size of 
# the gap
def big_map_2(gap_size = 20):
    # -------------------------- Basic Game Properties -------------------------- #
    # --------------------------- Create the Screen ----------------------------- #

    # define size of the app screen
    screen_size = (window_height, window_width) = 800, 800

    # define the grid AKA world size AKA number of nodes
    world_size = (world_height, world_width) = 200, 200

    # In the grid's (row, column) format
    start_location = (20, 20)
    goal_location = (180, 20)
    
    # ---------------------------- Create the World ----------------------------- #
    # this is a representation of the world. See world_definition.py for more info
    world = world_class(world_height, world_width, start_location, goal_location, screen_size)

    # --------------------------- Create the Screen ----------------------------- #
    # This comes from screen_helper_functions.py and uses pygame
    screen = make_screen(world, screen_size)

    
    # ---------------------------- Define the Walls ----------------------------- #
    gap_start = world_width//2 - gap_size//2
    gap_end = gap_start + gap_size

    wall_thickness = 6
    mid = world_height//2
    thic_1 = mid - wall_thickness//2
    thic_2 = mid + wall_thickness//2

    wall_loc_1 = [(i,j) for i in range(thic_1, thic_2) for j in range(0, gap_start)]
    wall_loc_2 = [(i,j) for i in range(thic_1, thic_2) for j in range(gap_end, 200)]
    wall_loc = wall_loc_1 + wall_loc_2
    for wall in wall_loc:
        pygame.draw.rect(screen, (0,0,0), (wall[1]*world.pixel_width, wall[0]*world.pixel_height, world.pixel_width, world.pixel_height))
        world.grid[wall[0]][wall[1]].wall = True
    pygame.display.flip()

    
    # --------------------- Compile Each Node's Neighbors ----------------------- #
    # Once again, see world_definition.py for more info
    world.compile_neighbors()

    return world, screen



#---------------------------------------------------------------------------------------------------------#
#--------------------------------------- Interactive Walls -----------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
def interactive_map(world_size, screen_size):
    # -------------------------- Basic Game Properties -------------------------- #
    # --------------------------- Create the Screen ----------------------------- #

    # In the grid's (row, column) format
    start_location = (0, 0)
    goal_location = (world_size[0]//2, world_size[1]//2)
    
    # ---------------------------- Create the World ----------------------------- #
    # this is a representation of the world. See world_definition.py for more info
    world = world_class(world_size[0], world_size[1], start_location, goal_location, screen_size)

    # --------------------------- Create the Screen ----------------------------- #
    # This comes from screen_helper_functions.py and uses pygame
    screen = make_screen(world, screen_size)

    # ---------------------------- Define the Walls ----------------------------- #
    ###### User Input ######
    start_path_planning = False
    mouse_clicked = False

    while not start_path_planning:
        # Look at all of the user interactions
        for event in pygame.event.get():
            # Figure out what kind of input the user sent
            match event.type:
                case pygame.MOUSEBUTTONDOWN:
                    world.add_wall(screen)
                    mouse_clicked = True
                # Mouse movement or clicks means we should add walls
                case pygame.MOUSEMOTION:
                    if mouse_clicked:
                        world.add_wall(screen)
                case pygame.MOUSEBUTTONUP:
                    mouse_clicked = False
                # Pressing any keyboard key means we should start the planning
                case pygame.KEYDOWN:
                    start_path_planning = True
                # Last option is to end the game
                case pygame.quit:   
                    print("quitting")
                    pygame.quit()
                    sys.exit()

    
    # --------------------- Compile Each Node's Neighbors ----------------------- #
    # Once again, see world_definition.py for more info
    world.compile_neighbors()

    return world, screen