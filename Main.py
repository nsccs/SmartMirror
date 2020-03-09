from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from gui.widget.Widget import Widget
from kivy.config import Config
import GetCalendar
import GetWeather
import GetDateTime

"""
    :author Luan Ta
    :version beta - 1.1.0 - 03/08/2020
    Main class of the program. Executes the GUI display.
"""
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
UPDATE_INTERVAL_WEATHER_CALENDER = 3600  # in seconds
UPDATE_INTERVAL_TIME = 1  # in seconds


class Main(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', str(WINDOW_WIDTH))
        Config.set('graphics', 'height', str(WINDOW_HEIGHT))
        self.layout = BoxLayout(orientation='vertical', size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.widget = Widget(self.layout, 3)
        self.widget.change_background(0, 0.3, 0.5, 1)
        self.update_calender_weather()
        self.update_time()
        Clock.schedule_interval(self.update_time, UPDATE_INTERVAL_TIME)
        Clock.schedule_interval(self.update_calender_weather, UPDATE_INTERVAL_WEATHER_CALENDER)

    def update_calender_weather(self, *args):
        self.widget.add_image(GetWeather.get_weather_img(), 300, 300, 100, 100)
        self.widget.change_panel_text(GetWeather.get_weather(), 2)
        self.widget.change_panel_text(GetCalendar.get_events(5), 3)

    def update_time(self, *args):
        self.widget.change_panel_text(GetDateTime.get_time(), 1)

    def build(self):
        return self.layout


if __name__ == '__main__':
    main = Main()
    main.run()
