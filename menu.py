from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.label import Label

def init_middle_line(self):
    with self.canvas.before:
        Color(.5, .5, .5)
        self.middle_line.append(Line())


def update_middle_line(self):
    actual_menu_height = self.height * self.menu_line_height
    x1, y1 = self.width / 2 - self.middle_line_width / 2, 0
    # x2, y2 = self.width/2 - self.middle_line_width/2, self.height - actual_menu_height
    x2, y2 = self.width / 2 - self.middle_line_width / 2, self.height
    self.middle_line[0].points = (x1, y1, x2, y2)
    self.middle_line[0].width = self.middle_line_width


def init_menu_line(self):
    with self.canvas.before:
        Color(.75, .75, .75)
        self.menu.append(Line())


def update_menu_line(self):
    actual_menu_height = self.height * self.menu_line_height
    x1, y1 = 0, self.height - actual_menu_height
    x2, y2 = self.width, self.height - actual_menu_height
    self.menu[0].points = (x1, y1, x2, y2)
    self.menu[0].width = self.menu_line_width


def init_score(self):
    with self.canvas.before:
        Color(1, 1, 1)
        for i in range(0, 2):
            self.score.append(Label())


def update_score_text(self):
    self.score_text_1 = str(self.score_number[0])
    self.score_text_2 = str(self.score_number[1])

