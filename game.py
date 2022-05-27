"""
A game with the possibility to move a player around the map

Steps: 
-Define a map, and parts for the player walk
-Define a entity, starting with the player
-make the player walk around the defined world.
"""
import keyboard
import time

class Game():

    def run_game(self):
        screen = Screen()
        player = Player(skin = 'O')
        done = False

        while not done:

            time.sleep(0.2)
            print("\x1b[2J\x1b[1;1H")

            screen.world[player.position_y][player.position_x] = player.skin

            print('*' * 10)
            screen.printworld()
            print('*' * 10)

            screen.world[player.position_y][player.position_x] = ' '
            
            print('Type your next move with w, a, s or d ')
            print('Press "x" to stop ')

            while True:
                if keyboard.is_pressed('x'):
                    done = True
                    break
                if keyboard.is_pressed('w'):
                    player.move_up()
                    break
                if keyboard.is_pressed('s'):
                    player.move_down()
                    break
                if keyboard.is_pressed('d'):
                    player.move_right()
                    break
                if keyboard.is_pressed('a'):
                    player.move_left()
                    break

        


class Screen():
    world = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    default_world = [
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


class Entity():

    def __init__(self, position_x = 0, position_y = 0, skin = str):
        self.position_x = position_x
        self.position_y = position_y
        self.skin = skin

    def move_right(self):
        if not self.position_x == 9:
            self.position_x += 1
    
    def move_left(self):
        if not self.position_x == 0:
            self.position_x -= 1
    
    def move_up(self):
        if not self.position_y == 0:
            self.position_y -= 1
    
    def move_down(self):
        if not self.position_y == 4:
            self.position_y += 1
        
    

class Player(Entity):
    pass    
        




game = Game()
game.run_game()