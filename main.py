from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '680')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Ellipse
from kivy.properties import Clock, StringProperty
from kivy.metrics import dp
import random

class MainWidget(RelativeLayout):
    from user_actions import on_keyboard_up, on_touch_up, on_touch_down, keyboard_closed, on_keyboard_down
    from menu import init_middle_line, init_score, init_menu_line, update_middle_line, update_menu_line, update_score_text
    from paddles import init_paddles, update_paddle_1, update_paddle_2, paddles_top_or_bottom

    last_width = 1280
    last_height = 680

    middle_line = []
    middle_line_width = 1

    menu = []
    menu_line_height = .05
    menu_line_width = 1

    score = []
    score_text_1 = StringProperty("0")
    score_text_2 = StringProperty("0")
    score_number = [0, 0]
    score_text_padding = dp(5)
    score_text_spacing = dp(30)
    score_font_size = dp(30)

    paddles = []
    paddles_width = 5
    paddles_height = .2
    paddle_speed = 10

    paddle_1_offset = 0
    paddle_1_moving = 0
    paddle_1_stop = False

    paddle_2_offset = 0
    paddle_2_moving = 0
    paddle_2_stop = False

    ball = []
    ball_size = {"normal": .025}
    ball_speed_x = 6
    default_ball_speed_x = 6
    ball_speed_y = 6
    default_ball_speed_y = 6
    ball_moving = False

    game_start = True
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_middle_line()
        self.init_menu_line()
        self.init_score()
        self.init_paddles()
        if self.is_desktop:
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1 / 60)


    def is_desktop(self):
        if platform in ("linux", "win", "macosx"):
            return True
        else:
            return False

    def start(self):
        print("Start")
        self.game_start = True

    def init_ball(self):
        with self.canvas:
            Color(1,1,1,1, mode='rgba')
            self.ball = Ellipse()

    def update_ball(self):
        r = self.ball_size["normal"] * self.height
        x, y = self.ball.pos[0] + self.ball_speed_x, self.ball.pos[1] + self.ball_speed_y

        if self.ball_hit_y(y):
            x, y = self.ball.pos[0] + self.ball_speed_x, self.ball.pos[1] + self.ball_speed_y
        if self.ball_hit_x(x, y):
            x, y = self.ball.pos[0] + self.ball_speed_x, self.ball.pos[1] + self.ball_speed_y

        self.ball.pos = (x, y)

    def ball_hit_x(self, x, y):
        r = self.ball_size["normal"] * self.height
        r += r
        if x <= 0:
            if self.paddles[0].points[1] - r <= y <= self.paddles[0].points[3]:
                self.ball_speed_x *= -1.1
                return True
            else:
                self.score_number[1] += 1
                self.score_text_2 = str(self.score_number[1])
                self.ball_moving = False
                return False

        far_right = self.width - r - self.paddles[0].width
        if x >= far_right:
            if self.paddles[1].points[1] - r <= y <= self.paddles[1].points[3]:
                self.ball_speed_x *= -1.1
                return True
            else:
                self.score_number[0] += 1
                self.score_text_1 = str(self.score_number[0])
                self.ball_moving = False

    def ball_move_to_center(self):
        r = self.ball_size["normal"] * self.height
        random_y = random.randint(10, 90) / 100
        x, y = self.width / 2 - r, self.height * random_y - r
        self.ball.pos = (x, y)
        self.ball.size = 2 * r, 2 * r

    def ball_hit_y(self, y):
        r = self.ball_size["normal"] * self.height
        if y >= self.height - (r+r) or y <= 0:
            self.ball_speed_y *= -1.05
            return True
        else:
            return False

    def first_ball_move(self):
        self.ball_speed_x = self.default_ball_speed_x
        self.ball_speed_y = self.default_ball_speed_y
        if not self.ball_moving:
            dirrection_random = random.randint(0, 1)
            if dirrection_random == 0:
                self.ball_speed_x *= -1
                self.ball_speed_y *= -1
            elif dirrection_random == 1:
                self.ball_speed_x *= 1
                self.ball_speed_y *= 1
            self.ball_moving = True

    def update(self, dt):
        self.update_middle_line()
        # self.update_menu_line()
        self.update_score_text()
        self.update_paddle_1()
        self.update_paddle_2()

        if self.game_start:
            self.paddles_top_or_bottom()

            if not self.ball_moving:
                self.first_ball_move()
                if self.ball == []:
                    self.init_ball()
                self.ball_move_to_center()
            self.update_ball()


        if self.height != self.last_height:
            self.paddle_speed /= self.last_height/self.height
            # self.score_font_size /= self.last_height / self.height
            self.last_height = self.height
        if self.width != self.last_width:
            self.ball_speed_x /= self.last_width/self.width
            self.ball_speed_y /= self.last_width / self.width
            self.last_width = self.width

class Pong(App):
    pass

Pong().run()