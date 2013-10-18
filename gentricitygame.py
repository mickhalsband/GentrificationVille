from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from house import House

__author__ = 'mick'

class MyToolbar(BoxLayout):
    def create_house(self):

        pass

class GentriCityGame(FloatLayout):
    house = ObjectProperty()
    #
    #def animate_house(self):
    #    a = Animation(x=(self.house.x + 200), duration=2)
    #    a.start(self.house)

    def CreateHouse(self):
        a = 1
