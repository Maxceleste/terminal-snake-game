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


        comand = screen.print_initial_screen()

        attempts = 3
        fruit.randomized_position(player.tail, [player.position_y, player.position_x])
        screen.printgame(player, fruit, attempts, comand)

        while not done:
            attempts -= 1

            if len(player.tail) == 49:
                screen.print_win_screen()
                break

            if attempts == 0:
                done = screen.print_death_screen()
                print('You have no more attempts!')
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
                    print('You have to stop when you eat the fruit!')
                    break

                player_movement = player.move(movement)

                if [player.position_y , player.position_x] in player.tail:
                    done = screen.print_death_screen()
                    print('You hit yourself!')
                    break

                if not player_movement:
                    done = screen.print_death_screen()
                    break


                if not player.tail == []:
                    initial_position_y = player.tail[0][0]
                    initial_position_x = player.tail[0][1]
                    player.tail_movement(player_movement[0], player_movement[1])

            
                if [player.position_y , player.position_x] == [fruit.position_y, fruit.position_x]:
                    eated_fruit = True
                    player.new_tail(initial_position_y, initial_position_x)
                    fruit.randomized_position(player.tail, [player.position_y, player.position_x])
                    attempts = 3

                
                screen.printgame(player, fruit, attempts, comand)
                time.sleep(0.2)




game = Game()
game.run_game()