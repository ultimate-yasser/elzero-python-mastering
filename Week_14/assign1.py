class Game:

    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price
        self.price_in_pounds = self.price * 40


game_one = Game('Minecraft', 'Mojang', 2005, 50)

print(f'Game name is "{game_one.name}"', \
      f'Developer is "{game_one.developer}"', \
        f'Year is {game_one.year}', \
            f'Price in LE is {game_one.price_in_pounds}')