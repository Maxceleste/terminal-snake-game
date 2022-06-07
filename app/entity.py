import random

class Entity():
    position_x = int
    position_y = int

    def __init__(self, skin = str):
        self.skin = skin

    
        

class Player(Entity):
    position_y = 0
    position_x = 0
    tail = []

    def move_right(self):
        old_position = [self.position_y, self.position_x]
        if not self.position_x == 9:
            self.position_x += 1
            return old_position
        else:
            return False
    
    def move_left(self):
        old_position = [self.position_y, self.position_x]
        if not self.position_x == 0:
            self.position_x -= 1
            return old_position
        else:
            return False
    
    def move_up(self):
        old_position = [self.position_y, self.position_x]
        if not self.position_y == 0:
            self.position_y -= 1
            return old_position
        else:
            return False
    
    def move_down(self):
        old_position = [self.position_y, self.position_x]
        if not self.position_y == 4:
            self.position_y += 1
            return old_position
        else:
            return False
    
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
        self.tail.insert(0, [position_y, position_x])
    

    def tail_movement(self, new_position_y, new_position_x):
        last_tail = self.tail.pop(0)
        self.tail.append([new_position_y, new_position_x])
        return self.tail[0]

        

class Fruit(Entity):
    position_y = 0
    position_x = 0


    def randomized_position(self, tails, player_position):
        positions = []
        for y in range(5):
            for x in range(10):
                positions.append([y, x])
            
        positions.remove(player_position)
        for tail in tails:
            positions.remove(tail)
        try:
            new_position = random.choice(positions)
            self.position_y = new_position[0]
            self.position_x = new_position[1]
        except:

            self.position_y = None
            self.position_x = None