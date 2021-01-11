"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 20  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BRICK_ROWS_COLOR = 2
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 100  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 3  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.
FRAME_RATE = 10  # Define the pause time


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width - self.paddle.width) / 2,
                        self.window.height - paddle_offset)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)
        self.cube = GRect(10, 10)

        # Default initial velocity for the ball.
        self.dx = 0
        self.dy = 0
        # Create the reaming lives table
        self.lives_table = GLabel('Lives: 3')
        # Create score table
        self.score = 0
        self.score_table = GLabel("Score: " + str(self.score))
        self.score_table.font = "-30"
        # Calculate the total bricks and finish game when all bricks has been remove
        self.total_bricks = BRICK_ROWS*BRICK_COLS
        self.your_score = GLabel("Your Score: "+str(self.score))
        self.your_score.font = "-40"

        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)

        # Draw bricks.
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(brick_width, brick_height)
                self.brick.x = j * brick_width + j * brick_spacing
                self.brick.y = i * brick_height + i * brick_spacing
                self.brick.filled = True
                if i <= 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif 2 <= i <= 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif 4 <= i <= 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif 6 <= i <= 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif 8 <= i <= 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, self.brick.x, self.brick.y + BRICK_OFFSET)

    # Define paddle move function
    def paddle_move(self, event):
        if event.x - self.paddle.width / 2 <= 0:
            self.paddle.x = 0
        elif event.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    # Reset ball to the middle of window when game re-start
    def reset_ball(self):
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)

    # def bricks_cube(self):
    #     self.cube = GRect(10, 10)
    #     self.cube.filled = True
    #     self.window.add(self.cube, self.ball.x, self.ball.y)

    def start(self, event):
        global MAX_X_SPEED, INITIAL_Y_SPEED
        if self.dx != 0 and self.dy != 0:
            pass
        else:
            self.ball_velocity()

    # Define the ball moving velocity and giving random speed to increase game funny
    def ball_velocity(self):
        self.dx = random.randint(0, MAX_X_SPEED)
        self.dy = random.randint(INITIAL_Y_SPEED, MAX_X_SPEED)
        if random.random() > 0.5:
            self.dx = -self.dx
        if random.random() > 0.5:
            self.dy = -self.dy

    # Define the function about ball reflection event
    def ball_touch_something(self):
        ball_left_side = self.ball.x
        ball_right_side = self.ball.x + self.ball.width
        ball_upper_side = self.ball.y
        ball_lower_side = self.ball.y + self.ball.height
        is_ball_touch_bricks0 = self.window.get_object_at(ball_left_side, ball_upper_side)
        is_ball_touch_bricks1 = self.window.get_object_at(ball_left_side, ball_lower_side)
        is_ball_touch_bricks2 = self.window.get_object_at(ball_right_side, ball_upper_side)
        is_ball_touch_bricks3 = self.window.get_object_at(ball_right_side, ball_lower_side)
        if is_ball_touch_bricks0 is not None and is_ball_touch_bricks0 is not self.paddle \
                and is_ball_touch_bricks0 is not self.lives_table and is_ball_touch_bricks0 is not self.score_table\
                and is_ball_touch_bricks0 is not self.cube:
            self.window.remove(is_ball_touch_bricks0)
            self.score += 1
            self.total_bricks -= 1
            self.score_table.text = "Score: " + str(self.score)
            self.ball_velocity()
            # self.bricks_cube()

        elif is_ball_touch_bricks1 is not None and is_ball_touch_bricks1 is not self.paddle \
                and is_ball_touch_bricks1 is not self.lives_table and is_ball_touch_bricks1 is not self.score_table\
                and is_ball_touch_bricks1 is not self.cube:
            self.window.remove(is_ball_touch_bricks1)
            self.score += 1
            self.total_bricks -= 1
            self.score_table.text = "Score: " + str(self.score)
            self.ball_velocity()
            # self.bricks_cube()

        elif is_ball_touch_bricks3 is not None and is_ball_touch_bricks3 is not self.paddle \
                and is_ball_touch_bricks3 is not self.lives_table and is_ball_touch_bricks3 is not self.score_table\
                and is_ball_touch_bricks3 is not self.cube:
            self.window.remove(is_ball_touch_bricks3)
            self.score += 1
            self.total_bricks -= 1
            self.score_table.text = "Score: " + str(self.score)
            self.ball_velocity()
            # self.bricks_cube()

        elif is_ball_touch_bricks2 is not None and is_ball_touch_bricks2 is not self.paddle \
                and is_ball_touch_bricks2 is not self.lives_table and is_ball_touch_bricks2 is not self.score_table\
                and is_ball_touch_bricks2 is not self.cube:
            self.window.remove(is_ball_touch_bricks2)
            self.score += 1
            self.total_bricks -= 1
            self.score_table.text = "Score: " + str(self.score)
            self.ball_velocity()
            # self.bricks_cube()

        elif is_ball_touch_bricks1 is self.paddle and is_ball_touch_bricks1 is not self.cube:
            self.dy = -self.dy

        elif is_ball_touch_bricks3 is self.paddle and is_ball_touch_bricks3 is not self.cube:
            self.dy = -self.dy






