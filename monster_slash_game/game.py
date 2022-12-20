import random
from actors import Player, Enemy, Ogre, Imp

class Game:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def main(self):
        self.print_intro()
        self.play()

    def print_intro(self):
        print('''
                Monster Slash!!!

                Ready Player One?
                [Press Any Key to Continue...]
        ''')

    def print_linebreaks(self):
        print()
        print('*' * 60)
        print()

    def get_all_status(self):
        self.player.get_stats()
        for enemy in self.enemies:
                enemy.get_stats()

    def play(self):
        while True:
            self.print_linebreaks()
            self.get_all_status()
            self.print_linebreaks()
            next_enemy = random.choice(self.enemies)
            cmd = input('You see a {}. [r]un, [a]ttack, [p]ass?   '.format(next_enemy.kind))
            if cmd == 'r':
                print('{} runs away!'.format(self.player.name))
                print(self.player.hp)
                print('{} heals thyself!'.format(self.player.name))
                self.player.heal()
                print(self.player.hp)
            elif cmd == 'a':
                self.player.attacks(next_enemy)
                if not next_enemy.is_alive():
                    self.enemies.remove(next_enemy)
                if next_enemy.is_alive():
                    next_enemy.attacks(self.player)
            elif cmd == 'p':
                print('You are still thinking about the next move...')
                if random.randint(1,11) < 5:
                    next_enemy.attacks(self.player)
                else:
                    print('Luckily you dodged an attack')
            else:
                print('Please choose a valid option')
                break

            if self.player.hp < 0:
                print('Oh no! You lose!')
                break

            if not self.enemies:
                print('You have won! Congratulations!')
                break


if __name__ == '__main__':
    enemies = [
        Ogre('Bob', 1, 3),
        Imp('Alice', 1, 1)
    ]
    player = Player('Hercules', 1)

    Game(player, enemies).main()
