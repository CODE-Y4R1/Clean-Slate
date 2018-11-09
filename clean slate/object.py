import math
import libtcodpy as libtcod
import pyglet

from pathlib import Path

movepath = Path("resources/move.wav")

class Object:
    #this is a generic object: the player, a monster, an item, the stairs...
    #it's always represented by a character on screen.
    def __init__(self, x, y, glyph, color, name, blocks=False, opponent=None, direction = 'down',
                item=None, inventory=None):
        self.x = x
        self.y = y
        self.glyph = glyph
        self.color = color
        self.name = name
        self.blocks = blocks
        self.opponent = opponent
        self.direction = direction
        self.item = item
        self.inventory = inventory

        if self.item:
            self.item.owner = self

        if self.inventory:
            self.inventory.owner = self
 
    def move(self, dx, dy):
        #move by the given amount
        sound = pyglet.media.load(movepath,  streaming=False)
        sound.play()
        self.x += dx
        self.y += dy

    def move_towards(self, target_x, target_y, game_map, entities):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        if not (game_map.is_blocked(self.x + dx, self.y + dy) or
                    get_blocking_entities_at_location(entities, self.x + dx, self.y + dy)):
            self.move(dx, dy)

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
 
    def draw(self):
        #set the color and then draw the character that represents this object at its position
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.glyph, libtcod.BKGND_NONE)
 
    def clear(self):
        #erase the character that represents this object
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)

    def setGlyph(self, glyph, color = libtcod.white):
        self.glyph = glyph
        self.color = color

    def getGlyph(self):
        return{'glyph':self.glyph, 'color':self.color}

    def setDirection(self, direction):
        self.direction = direction