from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

__author__ = 'mick'

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