class Games:
    def __init__(self, games):
        self.games = games

    def show_games(self):
        if type(self.games) == list:
            print('I have many games')
            for game in self.games:
                print(f'-- {game}')
        
        elif type(self.games) == int:
                print(f'I have {self.games} games')
        else:
                print(f'I have one game called {self.games}')


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()

my_games_names.show_games()

my_games_count.show_games()