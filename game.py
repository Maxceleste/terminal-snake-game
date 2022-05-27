"""
snake game
"""
import time

class Game():


    def run_game(self):
        screen = Screen()
        done = False
        player = Player(skin = 'O')

        screen.printgame(player)

        while not done:

            if screen.world == screen.complete_world:
                print('Parabéns! Você completou tudo!')
                break

            print('Type your next move sequence with "w", "a", "s" and "d" ')
            print('Press "q" to stop ')

            move_sequence = input()
            if move_sequence == 'q':
                break

            for movement in move_sequence:
                player.move(movement)
                screen.printgame(player)
                time.sleep(0.2)
                
            
                

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

    complete_world = [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ]

    def printworld(self):
        number_y = 0
        print('  0 1 2 3 4 5 6 7 8 9 ') 
        print('----------------------') 
        for tile in self.world:
            tileprinted = str(number_y) + '|'

            for space in tile:
                tileprinted += space + ' ' 
            number_y += 1
   
            print(tileprinted)
        
    def printgame(self, player):

            print("\x1b[2J\x1b[1;1H")

            self.world[player.position_y][player.position_x] = player.skin

            self.printworld()

            self.world[player.position_y][player.position_x] = ' '


class Entity():
    position_x = int
    position_y = int

    def __init__(self, skin = str):
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
    position_y = 0
    position_x = 0
    
    def move(self, input): 
        
        moveset = {
            'w' : 'self.move_up()',
            's' : 'self.move_down()',
            'd' : 'self.move_right()',
            'a' : 'self.move_left()',
        }

        try:
            eval(moveset[input])
        except:
            pass

class Fruit(Entity):

    def randomized_position():
        pass       




game = Game()
game.run_game()