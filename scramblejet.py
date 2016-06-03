from kivy.uix.image import Image
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from projectile import Missile

class ScrambleJet(Image):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.center_x = touch.x
            touch.grab(self)
            return True

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.center_x = touch.x
            return True


    def shoot(self):
        '''Shoot straight up.'''
        missile = Missile()
        missile.center = (self.right, self.center_y)
        self.mainscreen.add_widget(missile)
        (fx, fy) = self.mainscreen.width, self.center_y
        missile.shoot(fx, fy, self.mainscreen)