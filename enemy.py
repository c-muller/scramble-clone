from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.logger import Logger


class Enemy(Image):
    def animate(self, tx, ty, target):
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
        if self.parent:
            Logger.info("enemy: " + str(self.parent))
            self.parent.enemies.remove(self)
            self.parent.remove_widget(self)

