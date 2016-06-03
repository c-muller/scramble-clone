from kivy.animation import Animation
from kivy.uix.image import Image


class Projectile(Image):
    '''Lauch this piece of ammunition towards a target object (`target`),
    located at coordinates (`tx`, `ty`).

    When the projectile reaches its target, it disappears. Collision handling is done elsewhere.

    The `target` object is used to determine which collide_projectile method to check for collision
    in the on_progress method of the projectile.
    '''

    def shoot(self, tx, ty, target):
        self.target = target
        self.animation = Animation(x=tx, y=ty)
        self.animation.bind(on_start=self.on_start)
        self.animation.bind(on_progress=self.on_progress)
        self.animation.bind(on_complete=self.on_stop)
        self.animation.start(self)

    def on_start(self, instance, value):
        pass

    def on_progress(self, instance, value, progression):
        pass

    def on_stop(self, instance, value):
        self.parent.remove_widget(self)


class Missile(Projectile):
    pass


# class Bomb(Projectile):
#     pass