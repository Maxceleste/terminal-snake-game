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
                initial_position_y = player.position_y
                initial_position_x = player.position_x


                if eated_fruit:
                    done = screen.print_death_screen()
                    break

                player_movement = player.move(movement)
                last_tail = [player.position_y, player.position_x]

                if [player.position_y , player.position_x] in player.tail:
                    done = screen.print_death_screen()
                    break

                if not player_movement:
                    done = screen.print_death_screen()
                    break


                if not player.tail == []:
                    initial_position_y = player.tail[0][0]
                    initial_position_x = player.tail[0][1]
                    last_tail = player.tail_movement(player_movement[0], player_movement[1])

            
                if [player.position_y , player.position_x] == [fruit.position_y, fruit.position_x]:
                    eated_fruit = True
                    player.new_tail(initial_position_y, initial_position_x)
                    fruit.randomized_position(player.tail, [player.position_y, player.position_x])


                screen.printgame(player, fruit, last_tail)
                time.sleep(0.2)



game = Game()
game.run_game()