"""
A game with the possibility to move a player around the map

Steps: 
-Define a map, and parts for the player walk
-Define a entity, starting with the player
-make the player walk around the defined world.
"""

class Game():
    world = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    def printworld(self):
        for tile in self.world:
            tileprinted = ''
            for space in tile:
                tileprinted += space
            print(tileprinted)


game = Game()
game.printworld()