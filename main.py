import kivy
from gentricitygame import GentriCityGame

kivy.require('1.0.7')

from kivy.app import App


class GentriGameApp(App):
    def build(self):
        game = GentriCityGame()
        #Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    GentriGameApp().run()
