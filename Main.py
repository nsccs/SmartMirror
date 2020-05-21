from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from gui.widget.Widget import Widget
from kivy.config import Config
from kivy.core.window import Window
import GetCalendar
from GetWeather import GetWeather
import GetDateTime

"""
    :author Luan Ta + Micheal Chung + NSC CS Club
    :version beta - 1.1.0 - 03/08/2020
    Main class of the program. Executes the GUI display.
"""
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
UPDATE_INTERVAL_WEATHER_CALENDAR = 10  # in seconds
UPDATE_INTERVAL_TIME = 1  # in seconds

textColor = [1, 1, 1, 1]

class Main(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', str(WINDOW_WIDTH))
        Config.set('graphics', 'height', str(WINDOW_HEIGHT))
        self.layout = StackLayout(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.weatherLabel = Label(text='abc', color=textColor)
        #self.weatherImageWidget = Widget(BoxLayout(), 1)
        self.calendarLabel = Label(text='def', color=textColor)
        self.timeLabel = Label(text='ghi', color=textColor)
        
        self.layout.add_widget(self.calendarLabel)
        self.layout.add_widget(self.weatherLabel)
        self.layout.add_widget(self.timeLabel)
        
        #self.update_CALENDAR_weather()
        #self.update_time()
        
        # Schedule task to refresh the widgets
        #Clock.schedule_interval(self.update_time, UPDATE_INTERVAL_TIME)
        #Clock.schedule_interval(self.update_CALENDAR_weather, UPDATE_INTERVAL_WEATHER_CALENDAR)

    def update_CALENDAR_weather(self, *args):
        weather = GetWeather()
        self.weatherLabel = Label(text=weather.get_description() + '\n' + weather.get_temp(), color=textColor)
        #self.widget.add_image(weather.get_icon(), WINDOW_HEIGHT / 2, WINDOW_WIDTH / 3, 200, 200)
        self.calendarLabel = Label(text=GetCalendar.get_events(5), color=textColor)

    def update_time(self, *args):
        self.timeLabel = Label(text=GetDateTime.get_time(), color=textColor)

    def build(self):
        return self.layout


if __name__ == '__main__':
    main = Main()
    #33333333333333333Window.fullscreen = True
    main.run()
