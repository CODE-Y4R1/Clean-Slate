import libtcodpy as libtcod
from game_states import GameStates

def handle_keys(key, game_state):
    if game_state == GameStates.PLAYER_TURN:
    	return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_MENU:
    	return handle_inventory_keys(key)
    
    	return{}

def handle_inventory_keys(key):
    index = key.c - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_player_turn_keys(key):
    key_char = chr(key.c)

    if key.vk == libtcod.KEY_UP:
        return {'move':(0, -1),'direction':'up'}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move':(0, 1),'direction':'down'}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move':(-1, 0),'direction':'left'}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move':(1, 0),'direction':'right'}

    if key_char == 'i':
        return {'inventory': True}


    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}