from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.properties import ObjectProperty, NumericProperty, ListProperty
from kivy.app import App
from kivy.atlas import Atlas
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
import random
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


class GateGuardianPlayer(Widget):
    score = NumericProperty(0)
    life = NumericProperty(30)
    kills = NumericProperty(0)
    MAX_SPEED = 7
    velocity = [0, 0]
    spriteCount = 1
    duration = 20
    counter = 0

    def move(self, velocity):
        polX = self.right
        polY = self.top
        if polX < 800 and polX > 0:
            self.center_x += velocity[0]
        if polY < 600 and polY > 0:
            self.center_y += velocity[1]
        if polX > 800:
            self.center_x = 800 - self.width / 1.5 + 3
        if (polX - self.width) < 0:
            self.center_x = self.width / 1.5 - 3
        if polY > 600:
            self.center_y = 600 - self.height / 1.5 + 3
        if polY - self.height < 0:
            self.center_y = self.height / 1.5 - 3
        
        if velocity[0] > 0: dir = "right"
        else : dir = "left" 
        source = "atlas://npc/move" + dir + str(self.spriteCount)
        self.counter += 1
        if(self.counter > self.duration):
            self.canvas.clear()
            self.spriteCount = self.spriteCount % 2 + 1
            with self.canvas:
                Rectangle(pos=self.pos, size=self.size, source=source)
            self.counter = 0

        self.canvas.clear()
        with self.canvas:
            Rectangle(pos=self.pos, size=self.size, source=source)

    def shoot(self, dir):
        pass

class Game(Widget):
    player = ObjectProperty(None)

    def init(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.pressed_keys = set()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(keycode[1])

    def _on_keyboard_up(self, keyboard, keycode):
        self.pressed_keys.remove(keycode[1])

    def velocity(self):
        v = self.player.velocity
        a = self.player.MAX_SPEED / 15

        for vel in self.pressed_keys:
            if(vel == 'w'):
                if v[1] < self.player.MAX_SPEED:
                    v[1] = v[1] + a
            elif(vel == 's'):
                if v[1] > -self.player.MAX_SPEED:
                    v[1] = v[1] - a
            if(vel == 'a'):
                if v[0] > -self.player.MAX_SPEED:
                    v[0] = v[0] - a
            elif(vel == 'd'):
                if v[0] < self.player.MAX_SPEED:
                    v[0] = v[0] + a
        if 'w' not in self.pressed_keys and 's' not in self.pressed_keys:
            v[1] = v[1] * 300/333
        if 'a' not in self.pressed_keys and 'd' not in self.pressed_keys:
            v[0] = v[0] * 300/333
        return v

    def update(self, dt):
        dir = self.velocity()
        self.player.move(dir)
    
    def on_touch_down(self, touch):
        print(touch.pos)
        self.player.shoot(touch.pos)
        return super().on_touch_down(touch)

  

class GameApp(App):

    def build(self):
        game = Game()
        game.init()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        #self.new_enemy_event = Clock.schedule_interval(game.add_monster, 5)
        return game


if __name__ == '__main__':
    GameApp().run()

