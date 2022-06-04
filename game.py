"""
snake game
"""
import time
from app.screen import Screen
from app.entity import Player, Fruit


class Game():


    def run_game(self):
        screen = Screen()
        done = False
        player = Player(skin = 'O')
        fruit = Fruit('F')

        screen.print_initial_screen()

        fruit.randomized_position(player.tail, [player.position_y, player.position_x])
        screen.printgame(player, fruit)

        while not done:

            if len(player.tail) == 49:
                screen.print_win_screen()
                break

            print('Type your next move sequence with "w", "a", "s" and "d" ')
            print('Press "q" to stop ')

            move_sequence = input()
            if move_sequence == 'q':
                screen.print_bye_screen()
                break

            eated_fruit = False
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
                
            
                
            
                    



game = Game()
game.run_game()