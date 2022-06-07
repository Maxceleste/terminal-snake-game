from . import arts

class Screen():
    world = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    def clear_world(self):
        self.world[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.world[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 
        self.world[2] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 
        self.world[3] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 
        self.world[4] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def update_world(self, player, fruit):
        try:
            self.world[fruit.position_y][fruit.position_x] = fruit.skin
        except:
            pass

        self.world[player.position_y][player.position_x] = player.skin
        for tail in player.tail:
            self.world[tail[0]][tail[1]] = 'X'


    def print_initial_screen(self):
        print("\x1b[2J\x1b[1;1H")

        print(arts.snake_logo)

        print('Type "Enter" to play or type "help" to learn how to play.')
        
        comand = input()
        if comand == 'debug':
            return True

        elif comand == 'help':
            print(arts.help_text)
            input('Type "Enter" to play')

        return False


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

    def printgame(self, player, fruit, attempts, debug = bool):

            print("\x1b[2J\x1b[1;1H")
            self.update_world(player, fruit)
            print('Attempts:', attempts - 1)
            print('Player lenght:', len(player.tail) + 1)

            if debug:  
                print(player.tail)
                print('posição y:', player.position_y)
                print('posição x:', player.position_x)
                for tile in self.world:
                    print(tile)


            if not player.tail == []:   
                self.printworld()
                self.clear_world()
                 

            else:
                self.printworld()  
                self.clear_world()  
        
    
    def print_death_screen(self):
        print("\x1b[2J\x1b[1;1H")
        
        print(arts.death_art)

        print('Try again later!')
        return True


    def print_bye_screen(self):
        print('Bye!')
    
    def print_win_screen(self):
        print(arts.win_art)
        print('You beat the game!')