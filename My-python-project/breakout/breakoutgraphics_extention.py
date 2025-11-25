"""
File: breakoutgraphics_extention.py
Name: Alice Liu
------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program plays a Python game 'breakout'. A ball will be bouncing around the GWindow
Players if the user click the mouse for the 1st time each round, and it will end at
if there is no more lives or bricks.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout_extention'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width)/2,
                        y=(self.window.height - paddle_offset))
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width)/2,     
                        y=(self.window.height - self.ball.height)/2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        self.score = 0
        self.started = False
        self.brick_count = brick_rows * brick_cols

        self.score_label = GLabel(f"Score: {self.score}")
        self.score_label.font = "-20"
        self.window.add(self.score_label, x=5, y=520)

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.handle_click)

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.bricks = GRect(width=brick_width, height=brick_height)
                self.bricks.filled = True
                if i//2 == 0:
                    self.bricks.fill_color = 'red'
                elif i//2 == 1:
                    self.bricks.fill_color = 'orange'
                elif i//2 == 2:
                    self.bricks.fill_color = 'yellow'
                elif i//2 == 3:
                    self.bricks.fill_color = 'green'
                elif i//2 == 4:
                    self.bricks.fill_color = 'blue'

                self.window.add(self.bricks, x=j*(BRICK_WIDTH+BRICK_SPACING),
                                y=BRICK_OFFSET+(BRICK_HEIGHT+BRICK_SPACING)*i)

    def paddle_move(self, event):
        if event.x <= self.paddle.width/2:    
            self.paddle.x = 0
        elif event.x >= self.window.width-self.paddle.width/2:   
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2    

    def handle_click(self, event):   
        if self.__dx == 0 and self.__dy == 0:
            if not self.started:
                self.started = True
                self.set_ball_velocity()

    def set_ball_velocity(self):   
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def reset_ball(self):   
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0
        self.started = False

    def ball_collide_objects(self):
        xs = [self.ball.x, self.ball.x + self.ball.width]
        ys = [self.ball.y, self.ball.y + self.ball.height]
        for x in xs:
            for y in ys:
                obj = self.window.get_object_at(x, y)
                if obj is not None:
                    if obj is self.paddle:
                        if self.__dy > 0:  
                            self.__dy = -self.__dy
                    elif obj is self.score_label:
                        self.__dy = -self.__dy

                    else:
                        self.window.remove(obj)
                        self.brick_count -= 1
                        self.__dy = -self.__dy
                        self.score += 1
                        self.score_label.text = f"Score: {self.score}"
                        if self.score % 10 == 0:
                            self.increase_speed()
                    return None

    def increase_speed(self):
        self.__dx *= 1.5
        self.__dy *= 1.5

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    # setter
    def set_dx(self):
        self.__dx *= -1   

    def set_dy(self):

        self.__dy *= -1
