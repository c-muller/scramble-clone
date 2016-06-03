from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, \
    ObjectProperty
from kivy.clock import Clock
from kivy.lang import Builder
from scramblejet import ScrambleJet
from enemy import Enemy
import random

Builder.load_file('sprites.kv')

# todo fix this
UP = 273
DOWN = 274
LEFT = 276
RIGHT = 275
MOVE_DISTANCE = 5
SHOOT = 32

class ScrambleGame(Widget):
    jet = ObjectProperty(None)
    enemy = ObjectProperty(None)
    enemies = list()
    keys_down = {UP: False, DOWN: False, LEFT: False, RIGHT: False, SHOOT: False}

    def update(self, dt):
        self.jet.move()

        if self.keys_down[UP] and self.jet.top < self.top:
            self.jet.center_y += MOVE_DISTANCE
        if self.keys_down[DOWN] and self.jet.y > self.y:
            self.jet.center_y -= MOVE_DISTANCE
        if self.keys_down[LEFT] and self.jet.x > self.x:
            self.jet.center_x -= MOVE_DISTANCE
        if self.keys_down[RIGHT] and self.jet.right < self.right:
            self.jet.center_x += MOVE_DISTANCE
        if self.keys_down[SHOOT]:
            self.jet.shoot()

    def schedule_enemy(self, dt):
        enemy = Enemy()
        enemy.center = (self.width - 20, self.center_y)
        self.add_widget(enemy)
        (fx, fy) = self.x, random.randint(self.y, self.top)
        enemy.animate(fx, fy, self)
        self.enemies.append(enemy)

    def key_down(self, keyboard, keycode, *args):
        self.keys_down[keycode] = True
        # print "got a key event: %s" % keycode

    def key_up(self, keyboard, keycode, *args):
        self.keys_down[keycode] = False

    def collide_projectile(self, projectile):
        '''Detect a collision with projectile. Loop through remaining children checking for collision'''
        for enemy in self.enemies:
            if enemy.collide_widget(projectile):
                # boom.pos = child.pos
                self.enemies.remove(enemy)
                self.remove_widget(enemy)
                # self.add_widget(boom)
                return True

        return False


class ScrambleApp(App):
    def build(self):
        game = ScrambleGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        Clock.schedule_interval(game.schedule_enemy, 20.0 / 60.0)
        Window.bind(on_key_down=game.key_down)
        Window.bind(on_key_up=game.key_up)
        return game


if __name__ == '__main__':
    ScrambleApp().run()
