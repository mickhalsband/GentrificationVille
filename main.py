import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation


class House(BoxLayout):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    image_sprite = ObjectProperty(None)

    def move(self):
        #self.pos = Vector(*self.velocity) + self.pos
        self.center = self.center_x + 1, self.center_y + 100
        #image_sprite.r
        #        self.center_x += 1


class GentriCityGame(FloatLayout):
    house = ObjectProperty()

    def animate_bunny(self):
        a = Animation(x=(self.house.x + 200), duration=2)
        a.start(self.house)


class GentriGameApp(App):
    def build(self):
        game = GentriCityGame()
        #Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    GentriGameApp().run()
