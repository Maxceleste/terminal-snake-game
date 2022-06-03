"""
snake game
"""
import time
import random

class Game():


    def run_game(self):
        screen = Screen()
        done = False
        player = Player(skin = 'O')
        fruit = Fruit('F')

        print("\x1b[2J\x1b[1;1H")

        print("""
        

███████ ███    ██  █████  ██   ██ ███████ 
██      ████   ██ ██   ██ ██  ██  ██      
███████ ██ ██  ██ ███████ █████   █████   
     ██ ██  ██ ██ ██   ██ ██  ██  ██      
███████ ██   ████ ██   ██ ██   ██ ███████ 
                                          
                                          

""")
        print('Type something to play!')
        input()

        
        fruit.randomized_position(player.tail, [player.position_y, player.position_x])
        screen.printgame(player, fruit)

        while not done:

            print('Type your next move sequence with "w", "a", "s" and "d" ')
            print('Press "q" to stop ')

            move_sequence = input()
            if move_sequence == 'q':
                break

            for movement in move_sequence:
                player_movement = player.move(movement)

                if [player.position_y , player.position_x] in player.tail:
                    done = screen.print_death_screen()
                    break

                if not player_movement:
                    done = screen.print_death_screen()
                    break 

                screen.printgame(player, fruit)
                time.sleep(0.2)
                
            
                

class Screen():
    world = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    def printworld(self):
        number_y = 0
        print('  0 1 2 3 4 5 6 7 8 9 ') 
        print('  --------------------') 
        for tile in self.world:
            tileprinted = str(number_y) + '|'

            for space in tile:
                tileprinted += space + ' ' 
            tileprinted += '|'
            number_y += 1
   
            print(tileprinted)
        print('  --------------------')

    def printgame(self, player, fruit):

            print("\x1b[2J\x1b[1;1H")

            self.world[fruit.position_y][fruit.position_x] = fruit.skin  
            self.world[player.position_y][player.position_x] = player.skin  
            for tail in player.tail:
                self.world[tail[0]][tail[1]] = 'X' 

            if not player.tail == []:   
                last_tail = player.tail_movement(player.position_y, player.position_x)
                self.printworld()
                self.world[last_tail[0]][last_tail[1]] = ' '  
            else:
                self.printworld()  
                self.world[player.position_y][player.position_x] = ' '

            


    
    def print_death_screen(self):
        
        print("""
        

██    ██  ██████  ██    ██     ██████  ██ ███████ ██████      
 ██  ██  ██    ██ ██    ██     ██   ██ ██ ██      ██   ██     
  ████   ██    ██ ██    ██     ██   ██ ██ █████   ██   ██     
   ██    ██    ██ ██    ██     ██   ██ ██ ██      ██   ██     
   ██     ██████   ██████      ██████  ██ ███████ ██████      
                                                              
                                                              

""")
        return True

            
            


class Entity():
    position_x = int
    position_y = int

    def __init__(self, skin = str):
        self.skin = skin

    def move_right(self):
        if not self.position_x == 9:
            self.position_x += 1
            return True
        else:
            return False
    
    def move_left(self):
        if not self.position_x == 0:
            self.position_x -= 1
            return True
        else:
            return False
    
    def move_up(self):
        if not self.position_y == 0:
            self.position_y -= 1
            return True
        else:
            return False
    
    def move_down(self):
        if not self.position_y == 4:
            self.position_y += 1
            return True
        else:
            return False
        

class Player(Entity):
    position_y = 0
    position_x = 0
    tail = []
    
    def move(self, input): 
        
        moveset = {
            'w' : 'self.move_up()',
            's' : 'self.move_down()',
            'd' : 'self.move_right()',
            'a' : 'self.move_left()',
        }

        try:
            return eval(moveset[input])
        except:
            return False
    
    def new_tail(self, position_y, position_x):
        self.tail.append([position_y, position_x])
    

    def tail_movement(self, new_position_y, new_position_x):
        last_tail = self.tail.pop(0)
        self.tail.append([new_position_y, new_position_x])
        return last_tail

        

class Fruit(Entity):
    position_y = 0
    position_x = 0


    def randomized_position(self, tail, player_position):
        while True:
            self.position_y = random.randrange(5)
            self.position_x = random.randrange(10)
            fruit_position = [self.position_x, self.position_y]

            if fruit_position in tail or fruit_position == player_position:
                continue 
            else:
                break




game = Game()
game.run_game()