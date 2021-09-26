from kivy.uix.widget import Widget
from Player import Player

class Game(Widget):

    def init(self):
        self.size = (600, 800)
        player = Player()
        self.add_widget(player)

    def update(self, dt):
        pass