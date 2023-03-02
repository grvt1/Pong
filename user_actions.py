def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'down' and self.paddles[1].points[1] >= 0:
        self.paddle_2_moving = -1 * self.paddle_speed
    elif keycode[1] == 'up' and self.paddles[1].points[3] <= self.height:
        self.paddle_2_moving = self.paddle_speed

    if keycode[1] == 's' and self.paddles[0].points[1] >= 0:
        self.paddle_1_moving = -1 * self.paddle_speed
    elif keycode[1] == 'w' and self.paddles[0].points[3] <= self.height:
        self.paddle_1_moving = 1 * self.paddle_speed
    return True


def on_keyboard_up(self, keyboard, keycode):
    if keycode[1] == "down" or keycode[1] == "up":
        self.paddle_2_moving = 0
    if keycode[1] == "w" or keycode[1] == "s":
        self.paddle_1_moving = 0
    return True


def on_touch_down(self, touch):
    pass


def on_touch_up(self, touch):
    pass