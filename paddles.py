from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

def init_paddles(self):
    with self.canvas:
        Color(1, .3, .3)
        self.paddles.append(Line())
        Color(.3, .3, 1)
        self.paddles.append(Line())


def paddles_top_or_bottom(self):
    if self.paddles[0].points[1] <= 0:
        self.paddle_1_moving = 0
    if self.paddles[0].points[3] >= self.height:
        self.paddle_1_moving = 0

    if self.paddles[1].points[1] <= 0:
        self.paddle_2_moving = 0
    if self.paddles[1].points[3] >= self.height:
        self.paddle_2_moving = 0
    return True


def update_paddle_1(self):
    paddles_height = self.height * self.paddles_height
    offset = self.paddle_1_offset + self.paddle_1_moving
    x1, y1 = 0, (self.height / 2 - paddles_height / 2) + offset
    x2, y2 = 0, (self.height / 2 + paddles_height / 2) + offset

    self.paddles[0].points = (x1, y1, x2, y2)
    self.paddles[0].width = self.paddles_width
    self.paddle_1_offset = offset


def update_paddle_2(self):
    paddles_height = self.height * self.paddles_height
    offset = self.paddle_2_offset + self.paddle_2_moving
    x1, y1 = self.width, (self.height / 2 - paddles_height / 2) + offset
    x2, y2 = self.width, (self.height / 2 + paddles_height / 2) + offset
    self.paddles[1].points = (x1, y1, x2, y2)
    self.paddles[1].width = self.paddles_width
    self.paddle_2_offset = offset
