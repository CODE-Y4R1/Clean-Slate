import libtcodpy as libtcod
from enum import Enum
from game_states import GameStates
from menus.menus import inventory_menu

#BAR FUNCTION: Should be good for up to 4 digits (1000s), given 2 charspaces to the right.
#TODO: When value exceeds maximum, add one more # to the right and make all of them golden.
def render_bar(panel, x, y, total_width, name, value, maximum, bar_color):
    bar_width = int(float(value) / maximum * total_width)

    libtcod.console_print(panel, x, y, name +':')
    div = maximum / 10
    v = value / div
    z = 0
    while(z < 10):
        if(z < v):
            libtcod.console_put_char_ex(panel, 1+x+z+len(name), y, '#', bar_color, libtcod.black)
        else: libtcod.console_put_char_ex(panel, 1+x+z+len(name), y, '#', libtcod.gray, libtcod.black)
        z = z+1


    libtcod.console_set_default_foreground(panel, libtcod.white)
    libtcod.console_print_ex(panel, int(1 + x + total_width), y, libtcod.BKGND_NONE, libtcod.CENTER,
                             '{0}/{1}'.format(value, maximum))

def render_all(con, panel, objects, player, game_map, screen_width, screen_height, bar_width, panel_height, panel_y, colors, game_state):
    # Draw all the tiles in the game map
    for y in range(game_map.height):
        for x in range(game_map.width):

            tile = game_map.tiles[x][y]
            wall = tile.block_sight

            libtcod.console_set_default_foreground(con, tile.color)
            draw_tile(con, x, y, tile)

          #  if wall:
            #    #libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
           #     libtcod.console_put_char(con, x, y, object.glyph, libtcod.BKGND_NONE)
           # else:
           #     libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)

    # Draw all objects in the list
    for object in objects:
        draw_object(con, object)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

    if game_state == GameStates.PLAYER_MENU:
        inventory_menu(con, 'Press the key next to an item to use it, or Esc to cancel.\n',
                       player.inventory, 50, screen_width, screen_height)


    #Draw Info Panel

    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_clear(panel)

    #HP BAR
    render_bar(panel, 40, 1, bar_width, 'HP', player.opponent.hp, player.opponent.max_hp,
               libtcod.dark_green)
    #MP BAR
    render_bar(panel, 40, 2, bar_width, 'MP', player.opponent.mp, player.opponent.max_mp,
               libtcod.dark_blue)

    libtcod.console_blit(panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)


def clear_all(con, objects):
    for object in objects:
        clear_object(con, object)


def draw_object(con, object):
    libtcod.console_set_default_foreground(con, object.color)
    libtcod.console_put_char(con, object.x, object.y, object.glyph, libtcod.BKGND_NONE)


def clear_object(con, object):
    # erase the character that represents this object
    libtcod.console_put_char(con, object.x, object.y, ' ', libtcod.BKGND_NONE)

def draw_tile(con, x, y, tile):
    libtcod.console_put_char(con, x, y, tile.glyph, libtcod.BKGND_NONE)