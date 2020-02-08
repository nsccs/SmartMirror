
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from gui.widget.Widget import Widget
from kivy.config import Config
import kivy
kivy.require('1.11.1')

"""
    :author Luan Ta
    :version initial - 0.0.2 - 01/30/2020
    Main class of the program. Executes the GUI display.

    :TODO
        Change background color- DONE
        Transitioning text using Queue
        Support for image - DONE
        Support for touchscreen-interaction
        Linux testing - DONE
        MORE FEATURE-CREEPS
"""
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720


class Main(App):
    def build(self):
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', str(WINDOW_WIDTH))
        Config.set('graphics', 'height', str(WINDOW_HEIGHT))
        layout = BoxLayout(orientation='vertical', size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        widget = Widget(layout, 12)
        widget.change_background(0, 0, 0, 1)
        widget.change_panel_text("[color=#00ffec][size=24]Just call this function[/size][/color]", 1)
        widget.change_panel_text("[color=#d8ff00][size=20]And you can add any text with markup style[/size][/color]", 2)
        widget.change_panel_text("[color=#008bff][size=16]Change sizes, font, color[/size][/color]", 3)
        widget.change_panel_text("[color=#a600ff][size=12]Even color![/size][/color][/color]", 4)
        widget.add_new_panel()
        widget.add_image("hw.PNG", 250, 600, 100, 100)

        widget.remove_panel(4)

        return layout


if __name__ == '__main__':
    Main().run()
