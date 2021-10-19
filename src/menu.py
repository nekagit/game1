from kivy.app import App
from kivy.clock import Clock
from Game import Game
from Player import Player
from LevelTempel import LevelTempel
from Platform import Platform


class MenuApp(App):

    def build(self):
        game = Game()
        game.init()
        return game


if __name__ == '__main__':
    MenuApp().run()
