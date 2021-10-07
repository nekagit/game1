from kivy.app import App
from kivy.clock import Clock
from Game import Game

class MenuApp(App):

    def build(self):
        game = Game()
        game.init()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    MenuApp().run()

