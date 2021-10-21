from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from typing import List
from kivy.properties import ObjectProperty, ListProperty
from kivy.core.window import Window

from Platform import Platform
Window.size = (600, 500)
size = Window.size

class LevelTempel(Widget):
    player = ObjectProperty(None)
    platform = ObjectProperty(None)
    source = StringProperty("")
    size = size

    def init(self):
        self.player.init()

    def refresh(self):
        self.player.handleInput()
        self.player.move(self, self.platform)
        self.player.animate()

    # def direction(self):
    # def handleInput(self):
    # def move(self, wall: Widget, object: Widget):
    # def interpolated_collision(self, wid: Widget, dir):
    # def detectCollision(self, objects, dir):
    # def animate(self)
