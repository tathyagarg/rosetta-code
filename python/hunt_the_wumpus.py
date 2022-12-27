# https://rosettacode.org/wiki/Hunt_the_Wumpus

import random
import string

def lose(text):
    print(text)
    quit()

class Game:
    rooms = {
        'A': ('B', 'H', 'E'),
        'B': ('A', 'J', 'C'),
        'C': ('L', 'B', 'D'),
        'D': ('C', 'E', 'N'),
        'E': ('D', 'A', 'F'),
        'F': ('E', 'G', 'O'),
        'G': ('H', 'F', 'Q'),
        'H': ('A', 'G', 'I'),
        'I': ('H', 'R', 'J'),
        'J': ('I', 'K', 'B'),
        'K': ('S', 'L', 'J'),
        'L': ('M', 'C', 'K'),
        'M': ('N', 'T', 'L'),
        'N': ('O', 'D', 'M'),
        'O': ('P', 'N', 'F'),
        'P': ('O', 'Q', 'T'),
        'Q': ('G', 'P', 'R'),
        'R': ('Q', 'S', 'I'),
        'S': ('R', 'T', 'K'),
        'T': ('P', 'S', 'M')
    }

    def __init__(self):
        self.player_room: str = 'A'
        self.wumpus_room: str = random.choice(string.ascii_uppercase[1:20])
        self.bat_1: str = random.choice(string.ascii_uppercase[1:20])
        self.bat_2: str = random.choice(string.ascii_uppercase[1:20])
        self.pit_1: str = random.choice(string.ascii_uppercase[1:20])
        self.pit_2: str = random.choice(string.ascii_uppercase[1:20])

        self.arrows: int = 5

    def move_player(self):
        adjacent_rooms = Game.rooms[self.player_room]

        room = input('To which room? ').upper()
        while room not in adjacent_rooms:
            room = input('To which room? ').upper()

        self.player_room = room
        if self.wumpus_room == self.player_room:
            lose('You walked into the room with Wumpus and it devoured you!')
        elif self.bat_1 == self.player_room or self.bat_2 == self.player_room:
            curr = self.player_room

            self.player_room = random.choice(string.ascii_uppercase[:20])
            while self.player_room in [self.wumpus_room, curr]:
                self.player_room = random.choice(string.ascii_uppercase)

            print(f"A bat picked you up and put you in {self.player_room}!")
            return
        elif self.pit_1 == self.player_room or self.pit_2 == self.player_room:
            lose('You fell into a pit and died..')


    def player_move(self):
        adjacent_rooms = Game.rooms[self.player_room]
        print("="*25)
        print(f'You are in room {self.player_room}')
        print(f'This room is connected to: ')
        print(f'\t{".".join(Game.rooms[self.player_room])}')
        if self.wumpus_room in adjacent_rooms:
            print('You smell something terrible nearby.')
        if self.bat_1 in adjacent_rooms or self.bat_2 in adjacent_rooms:
            print('You hear a rustling.')
        if self.pit_1 in adjacent_rooms or self.pit_2 in adjacent_rooms:
            print('You feel a cold wind blowing from a nearby cavern.')

        s_m = input('Shoot (S) or Move (M)? ').upper()
        while s_m not in ['S', 'M']:
            s_m = input('Shoot (S) or Move (M)? ').upper()

        if self.arrows != 0:
            if s_m == 'S':
                print(f'You have {self.arrows} arrows')
                shoot_room = input('Which room to shoot in? ').upper()
                while shoot_room not in adjacent_rooms:
                    shoot_room = input('Which room to shoot in? ').upper()

                self.arrows -= 1
                if shoot_room == self.wumpus_room:
                    print("Prick! The Wumpus is dead!")
                    return
                else:
                    wumpus_moves = random.randint(1, 4) <= 3
                    if wumpus_moves:
                        self.wumpus_room = random.choice(Game.rooms[self.wumpus_room])
                        if self.wumpus_room == self.player_room:
                            lose('The Wumpus was disturbed by arrow and moved. He moved into your room and devoured you!')
                            return
            else:
                self.move_player()
        else:
            if s_m == 'S':
                print('You don\'t have any arrows!')
            else:
                self.move_player()
        self.player_move()

game = Game()
game.player_move()
