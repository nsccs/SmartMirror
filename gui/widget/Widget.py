from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

"""
    :author Luan Ta
    A Widget Object provides ease of use for the Kivy library.
"""


class Widget:

    def __init__(self, layout: BoxLayout, num_of_panels: int):
        """
        Create a Widget Object to display texts and images. Define the number of labels used.
        :param layout: Parent of this Widget
        :param num_of_panels: number of panels. Subsequence panels will reduce the height of each panel.
        """
        self.panels = []
        self.num_of_panels = num_of_panels
        self.layout = layout
        for i in range(num_of_panels):
            tmp = Label(text="Panel " + str(i + 1) + ": Call change_panel_text()!", markup=True, pos_hint={'top': 1.0})
            self.layout.add_widget(tmp)
            self.panels.append(tmp)

    def change_panel_text(self, element: str, panel_num: int):
        """
        Change the text of the given Panel. Text can be embedded with Markup components.
        :param element: given text to be updated
        :param panel_num: the Panel to be updated
        """
        self.panels[panel_num - 1].text = element

    def change_background(self, r: float, g: float, b: float, a: float):
        """
        Change the Color of the background of this Widget and all labels
        :param r: Red component
        :param g: Green component
        :param b: Blue component
        :param a: Transparency
        """
        with self.layout.canvas.before:
            Color(rgba=(r, g, b, a))
            Rectangle(size=self.layout.size, pos=self.layout.pos)
        for i in range(self.num_of_panels):
            self.layout.remove_widget(self.panels[i])
            self.layout.add_widget(self.panels[i])

    def add_new_panel(self):
        """
        Add a new Panel to the Widget. Subsequence panels will reduce the height of each panel.
        """
        self.num_of_panels += 1
        tmp = Label(text="Panel " + str(self.num_of_panels) + ": Call change_panel_text()!",
                    markup=True, pos_hint={'top': 1.0})
        self.layout.add_widget(tmp)
        self.panels.append(tmp)

    def remove_panel(self, panel: int):
        """
        Remove a Panel from the Widget. Subsequence removals will increase the height of each panel.
        :param panel: Panel to remove
        :return: the removed Panel Object
        """
        tmp = self.panels[panel - 1]
        self.layout.remove_widget(tmp)
        self.num_of_panels -= 1
        return tmp

    def add_image(self, path: str, pos_x: int, pos_y: int, width: int, height: int):
        """
        Add an image to this Widget.
        :param path: the absolute/relative path to the image file
        :param pos_x: the X position of this image. Reference point (0,0) is the bottom-left point of the Window.
        :param pos_y: the Y position of this image. Reference point (0,0) is the bottom-left point of the Window.
        :param width: the width of this image
        :param height: the height of this image
        """
        if self.panels.__sizeof__() != 0:
            self.panels[0].add_widget(Image(source=path, pos=(pos_x, pos_y), size=(width, height)))
        else:
            print("NO PANEL AVAILABLE!")
