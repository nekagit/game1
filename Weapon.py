import pygame


class GateGuardianMonster(Widget):
    spriteCount = 1
    duration = 20
    counter = 0

    def move(self, player):
        self.velocity = (Vector(*player.pos) - self.pos) / \
            Vector(*player.pos).distance(self.pos) * 2
        if (not self.collide_widget(player)):
            self.pos = Vector(*self.velocity) + self.pos
        else:
            self.pos = (0, self.center_y)
            player.life -= 1
        
        if self.velocity[0] > 0: dir = "up"
        else : dir = "down" 
        source = "atlas://enemy/move" + dir + str(self.spriteCount)
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


class GateGuardianTree(Widget):
    pass


class GateGuardianGame(Widget):
    player = ObjectProperty(None)
    monsters = ListProperty([])
    trees = ListProperty([])
    score = ObjectProperty(None)

    def add_monster(self, *args):
        monsteri = GateGuardianMonster()
        monsteri.pos = (random.randint(0, 1000), random.randint(0, 1000))
        with monsteri.canvas:
            Color(random.uniform(0.5, 1.0), random.uniform(
                0.5, 1.0), random.uniform(0.5, 1.0))
        self.add_widget(monsteri)
        self.monsters.append(monsteri)

    def add_tree(self):
        tree = GateGuardianTree()
        tree.pos = (random.randint(0, self.width),
                    random.randint(0, self.height))
        with tree.canvas:
            Color(random.uniform(0.5, 1.0), random.uniform(
                0.5, 1.0), random.uniform(0.5, 1.0))
        self.add_widget(tree)
        self.trees.append(tree)

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

    def reset(self):
        self.player.pos = self.center

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

        if self.player.life <= 0:
            self.ids.score.text = "GAME OVER"
            exit()
        else:
            for i in range(0, len(self.monsters), 1):
                self.monsters[i].move(self.player)

            self.player.move(dir)
    
    def on_touch_down(self, touch):
        print(touch.pos)
        self.player.shoot(touch.pos)
        return super().on_touch_down(touch)


class GateGuardianApp(App):

    def build(self):
        game = GateGuardianGame()
        game.init()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        self.new_enemy_event = Clock.schedule_interval(game.add_monster, 5)
        return game


if __name__ == '__main__':
    GateGuardianApp().run()


####################################################################

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()




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