# Screen Helper Functions
#
# Helper functions for displaying information on the screen
#   make_screen - initialize the pygame screen
#   draw_path - highlights the path on the screen in green
#   draw_cost_values - display the value/cost of each node
#
# Author:
#   Travis Hainsworth
#   CSCI 3022 - Introduction to Robotics
#   CU Boulder
#   Fall 2024
import pygame


def make_screen(world, screen_size):
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 255, 0), (world.start[1]*world.pixel_width, world.start[0]*world.pixel_height, world.pixel_width, world.pixel_height))
    pygame.draw.rect(screen, (255, 0, 0), (world.goal[1]*world.pixel_width, world.goal[0]*world.pixel_height, world.pixel_width, world.pixel_height))
    pygame.display.flip()

    return screen


def draw_path(world, screen):
    goal_pos = world.goal
    node = world.grid[goal_pos[0]][goal_pos[1]]   
    while node.previous:        
        node = node.previous
        node_row = node.position[0]
        node_col = node.position[1]
        
        pygame.draw.rect(screen, (0,255,0), (node_col*world.pixel_width, node_row*world.pixel_height, world.pixel_width, world.pixel_height))
        pygame.display.flip()



def draw_cost_values(world, screen):
    
    font = pygame.font.Font(None, 20)

    list_o_nodes = [node for row in world.grid for node in row]
    for node in list_o_nodes:
        node_row = node.position[0]
        node_col = node.position[1]

        cost = node.true_cost
        text = font.render(str(cost), True, (0,0,0))

        rectangle = pygame.Rect(node_col*world.pixel_width, node_row*world.pixel_height, world.pixel_width, world.pixel_height)

        text_rect = text.get_rect(center=rectangle.center)


        screen.blit(text, text_rect)

    pygame.display.flip()  


def color_explore(world, screen):
    gray_color = (100, 100, 100)

    list_o_nodes = [node for row in world.grid for node in row]

    for node in list_o_nodes:
        if not node.wall and node.true_cost == float('inf'):
            node_row = node.position[0]
            node_col = node.position[1]

            pygame.draw.rect(screen, gray_color, (node_col*world.pixel_width, node_row*world.pixel_height, world.pixel_width, world.pixel_height))
    
    pygame.display.flip()


def update_RRT_graph(new_node, closest_node, world, screen):
    color = (40, 40, 40)
    # Draw a dot where the new node is:
    new_position = (new_node.position[1] * world.pixel_height, new_node.position[0] * world.pixel_width)
    pygame.draw.circle(screen, color, new_position, 2)

    # Draw a line between the new node and the closest node
    closest_position = (closest_node.position[1] * world.pixel_height, closest_node.position[0] * world.pixel_width)
    pygame.draw.line(screen, color, closest_position, new_position)

    pygame.display.flip()


def remove_RRT_graph(node_1, node_2, world, screen):
    color = (255, 255, 255)
    # Draw a white line between the two nodes
    pixel_1 = (node_1.position[1] * world.pixel_height, node_1.position[0] * world.pixel_width)
    pixel_2 = (node_2.position[1] * world.pixel_height, node_2.position[0] * world.pixel_width)
    
    pygame.draw.line(screen, color, pixel_1, pixel_2)

    pygame.display.flip()

def update_entire_rrt_screen(explored_nodes, world, screen):
    screen.fill((255, 255, 255))

    # Add start and goal
    pygame.draw.rect(screen, (0, 255, 0), (world.start[1]*world.pixel_width, world.start[0]*world.pixel_height, world.pixel_width*2, world.pixel_height*2))
    pygame.draw.rect(screen, (255, 0, 0), (world.goal[1]*world.pixel_width, world.goal[0]*world.pixel_height, world.pixel_width*2, world.pixel_height*2))

    # Add walls
    for wall in world.wall_list:
        pygame.draw.rect(screen, (0, 0, 0), (wall[1]*world.pixel_width, wall[0]*world.pixel_height, world.pixel_width, world.pixel_height))

    # Add tree
    for node in explored_nodes:
        if node.position != world.start:
            node_pixel = (node.position[1] * world.pixel_height, node.position[0] * world.pixel_width)
            pygame.draw.circle(screen, (0, 0, 0), node_pixel, 2)

            node_parent_pixel = (node.previous.position[1] * world.pixel_height, node.previous.position[0] * world.pixel_width)
            pygame.draw.circle(screen, (0, 0, 0), node_parent_pixel, 2)

            pygame.draw.line(screen, (0,0,0), node_pixel, node_parent_pixel)

    
    pygame.display.flip()
    
