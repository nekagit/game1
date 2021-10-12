from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.widget import Widget

class Platform(Widget):
    pass

class Game(Widget):
    player = ObjectProperty(None)
    fireballs = ListProperty([])
    platform = ObjectProperty(None)

    def init(self):
        self.player.init()

    def update(self, dt):
        self.player.move(self)
        self.player.animate()