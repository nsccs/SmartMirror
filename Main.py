from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from gui.widget.Widget import Widget
from kivy.config import Config
import GetCalendar
import GetWeather

"""
    :author Luan Ta
    :version initial - 0.0.2 - 01/30/2020
    Main class of the program. Executes the GUI display.

    :TODO
        Change background color- DONE
        Transitioning text using Queue - IN PROGRESS
        Support for image - DONE
        Support for touchscreen-interaction
        Linux testing - DONE
        MORE FEATURE-CREEPS
"""
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
UPDATE_INTERVAL = 60  # in seconds


class Main(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', str(WINDOW_WIDTH))
        Config.set('graphics', 'height', str(WINDOW_HEIGHT))
        self.layout = BoxLayout(orientation='vertical', size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.widget = Widget(self.layout, 2)
        self.widget.change_background(0, 0.3, 0.5, 1)
        self.update()
        Clock.schedule_interval(self.update, UPDATE_INTERVAL)

    def update(self, *args):
        self.widget.add_image(GetWeather.get_weather_img(), 250, 600, 100, 100)
        self.widget.change_panel_text(GetWeather.get_weather(), 1)
        self.widget.change_panel_text(GetCalendar.get_events(1), 2)

    def build(self):
        return self.layout


if __name__ == '__main__':
    main = Main()
    main.run()
