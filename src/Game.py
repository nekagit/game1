from typing import List
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.widget import Widget


class Game(Widget):
    level = ObjectProperty(None)

    def init(self):
        self.level.init()

    def update(self, dt):
        self.level.refresh()
