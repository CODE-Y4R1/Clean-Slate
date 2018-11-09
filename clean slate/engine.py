import libtcodpy as libtcod
import resources
import pyglet

pyglet.options['audio'] = ('directsound','silent')

from combat.opponent import Opponent
from object import Object
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import clear_all, render_all
from menus.inventory import Inventory
from menus.item import Item
from game_states import GameStates

def main():
    screen_width = 64
    screen_height = 32
    
    bar_width = 18
    panel_height = 4
    panel_y = screen_height - panel_height

    map_width = 30
    map_height = 30

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30


    colors = {
        'dark_wall': libtcod.Color(50, 50, 50),
        'dark_ground': libtcod.Color(150, 150, 150)
    }

    #Player starting add-ons
    player_stats = Opponent(hp=3000, mp=1000, defense = 2, power = 5)
    player_inventory = Inventory(4)

    #Player instantiation
    player = Object(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white, 'Player', blocks=True, opponent=player_stats,
    	            inventory = player_inventory)
   
    #Player stat change tests
    player.opponent.hp = 1500
    player.opponent.mp = 500

    npc = Object(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow, 'NPC')
    objects = [npc, player]

    libtcod.console_set_custom_font('testfont8x16_aa_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'Clean Slate', False)

    con = libtcod.console_new(screen_width, screen_height)
    panel = libtcod.console_new(screen_width, panel_height)

    game_map = GameMap(map_width, map_height)
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)

    #key = libtcod.console_wait_for_keypress(True)
    key = libtcod.console_check_for_keypress()
    mouse = libtcod.Mouse()

    game_state = GameStates.PLAYER_TURN
    previous_game_state = game_state

    while not libtcod.console_is_window_closed():
        
        render_all(con, panel, objects, player, game_map, screen_width, screen_height, bar_width, panel_height, panel_y, colors, game_state)

        libtcod.console_flush()
        clear_all(con, objects)

        #############################
        #Player Control Section
        #############################

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_RELEASE, key, mouse)
        action = handle_keys(key, game_state)

        move = action.get('move')
        direction = action.get('direction')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        inventory = action.get('inventory')

        if inventory:
            previous_game_state = game_state
            game_state = GameStates.PLAYER_MENU
            libtcod.console_print(panel, 0, 0, "INVENTORY")


        if move:

            dx, dy = move

            if direction == 'up':
                player.setGlyph('^')

            elif direction == 'down':
                player.setGlyph('v')

            elif direction == 'left':
                player.setGlyph('<')

            else: player.setGlyph('>')

            if not game_map.is_blocked(player.x + dx, player.y + dy) and player.direction == direction:
                player.move(dx, dy)


            if player.direction != direction:
                player.setDirection(direction)

        if exit:
            if game_state == GameStates.PLAYER_MENU:
               game_state = previous_game_state
            else:
                return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
     main()