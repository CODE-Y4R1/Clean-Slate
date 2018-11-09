import libtcodpy as libtcod
from map_objects.tile_ids import NameToID 
from map_objects.tile_glyphs import tile_glyph

class Tile:
    """
    A tile on a map. It may or may not be blocking, it has a glyph, it has a reference to which kind of Tile it is, and it may or may not block sight.
    """
    def __init__(self, blocked, tileID=1, glyph = 'x', color=libtcod.darkest_grey, block_sight=None):
        self.blocked = blocked
        self.tileID = tileID
        self.glyph = glyph
        self.color = color
        # By default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

    def setTile(self, name):
        if(name == 'FLOOR'):
            self.blocked = False
            self.block_sight = False
            self.tileID = 3
            self.glyph = '.'
            self.color = libtcod.white

        elif(name == 'WALL'):
            self.blocked = True
            self.block_sight = True
            self.tileID = 2
            self.glyph = 'O'
            self.color = libtcod.grey

        elif(name == 'BOUNDS'):
            self.blocked = True
            self.block_sight = True
            self.tileID = 1
            self.glyph = 'x'
            self.color = libtcod.darkest_grey

        else:
       	    self.blocked = True
            self.block_sight = True
            self.tileID = 1
            self.glyph = 'x'
            self.color = libtcod.darkest_grey




