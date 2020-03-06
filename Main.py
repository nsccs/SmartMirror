from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from gui.widget.Widget import Widget
from kivy.config import Config
import GetCalendar

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
UPDATE_INTERVAL = 1000  # in milliseconds


class Main(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', str(WINDOW_WIDTH))
        Config.set('graphics', 'height', str(WINDOW_HEIGHT))
        self.layout = BoxLayout(orientation='vertical', size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.widget = Widget(self.layout, 3)
        # widget.change_background(1, 0, 0, 1)
        self.widget.add_image("gui/hw.PNG", 250, 600, 100, 100)
        self.current_i = 0
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.widget.change_panel_text("Time: " + str(datetime.now().time()), 1)
        self.widget.change_panel_text(GetCalendar.get_events(1), 2)
        self.current_i += 1
        if self.current_i >= UPDATE_INTERVAL:
            Clock.unschedule(self.update)

    def build(self):
        return self.layout


if __name__ == '__main__':
    main = Main()
    main.run()
    # main.widget.change_panel_text(str(datetime.now().time()), 1)
    # main.widget.update_all_panel()
    # date_time = DateTimeInput(1)

    # process = TaskProcessor(2000, main.widget, [date_time])
