from game import Game, Player

def main() -> None:
    p1 = Player("Louis", "Zappa")
    p2 = Player("Chiko", "Neutron")
    game1 = Game(p1)
    print(game1.state)

    game1 = game1.attack().win_or_loose()
    print(game1.state)
    print(game1)
    print()

    game2 = Game(player=p2).attack().win_or_loose()
    print()
    print(game2)