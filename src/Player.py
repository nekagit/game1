from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty


class Player(Widget):
    score = NumericProperty(0)
    life = NumericProperty(30)
    kills = NumericProperty(0)
    source = StringProperty("")
    MAX_SPEED = 7
    velocity = [0, 0]
    counter = 0
    spriteIndex = 1
    pressed_keys = set()

    def init(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(keycode[1])

    def _on_keyboard_up(self, keyboard, keycode):
        self.pressed_keys.remove(keycode[1])

    def direction(self):
        v = self.velocity
        a = self.MAX_SPEED / 15
        for vel in self.pressed_keys:
            if(vel == 'w'):
                v[1] = a*25
            if(vel == 'a'):
                if v[0] > 0:
                    v[0] = 0
                if v[0] > -self.MAX_SPEED:
                    v[0] = v[0] - a
            elif(vel == 'd'):
                if v[0] < 0:
                    v[0] = 0
                if v[0] < self.MAX_SPEED:
                    v[0] = v[0] + a
        if(self.top - self.height > 0):
            if v[1] > -self.MAX_SPEED:
                v[1] = v[1] - a

        if 'a' not in self.pressed_keys and 'd' not in self.pressed_keys:
            v[0] = v[0] * 300/333

        return v

    def handleInput(self):
        for vel in self.pressed_keys:
            if(vel == 'r'):
                self.pos = [0, 0]

    def move(self, wall: Widget, object: Widget):
        objects = [object]
        velocity = self.direction()
        if self.top + velocity[1] < wall.top and self.top - self.height + velocity[1] > 0 and self.detectCollision(objects, "vertical"):
            self.top += velocity[1]
        if self.right + velocity[0] < wall.right and self.right - self.width + velocity[0] > 0 and self.detectCollision(objects, "horizontal"):
            self.right += velocity[0]
        self.velocity = velocity

    def detectCollision(self, objects, dir):
        is_colliding = False
        if dir == "vertical":
            dir = 1
        else:
            dir = 0
        for object in objects:
            if self.interpolated_collision(object, dir):
                is_colliding = True
        return not is_colliding

    def interpolated_collision(self, wid: Widget, dir):
        vel = self.direction()
        if self.right + vel[dir] < wid.x:
            return False
        if self.x - vel[dir] > wid.right:
            return False
        if self.top + vel[dir] < wid.y:
            return False
        if self.y + vel[dir] > wid.top:
            return False
        return True

    def animate(self):
        dir = "right"
        if self.velocity[0] < 0:
            dir = "left"
        self.source = "atlas://npc/move" + dir + str(self.spriteIndex)
        if self.counter % 30 == 0 and self.velocity[1] < 0:
            self.spriteIndex = self.spriteIndex % 2 + 1
            self.counter = 1
        self.counter += 1
