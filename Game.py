from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.widget import Widget

class GateGuardianGame(Widget):
    player = ObjectProperty(None)
    fireballs = ListProperty([])

    def init(self):
        self.player.init()

    def update(self, dt):
        self.player.move(self)
        self.player.animate()