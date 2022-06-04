from . import arts

class Screen():
    world = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    def print_initial_screen(self):
        print("\x1b[2J\x1b[1;1H")

        print(arts.snake_logo)

        print('Type "Enter" to play or type "help" to learn how to play.')
        
        comand = input()

        if comand == 'help':
            print(arts.help_text)
            input('Type "Enter to play"')


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
        print("\x1b[2J\x1b[1;1H")
        
        print(arts.death_art)

        print('Try again later!')
        return True


    def print_bye_screen(self):
        print('Bye!')
    
    def print_win_screen(self):
        print(arts.win_art)
        print('You beat the game!')