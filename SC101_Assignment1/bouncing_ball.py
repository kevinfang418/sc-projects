"""
File: bounching_ball.py
Name: Kevin Fang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
VY = 0
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
COUNT = 0
GAME_OVER = 3

"""
define window and ball in Global variable in order to used by everyone,
both of inside and outside function
"""
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
# define ball method so that ball will show in the window before onmouseclicked
    ball.filled = True
    ball.fill_color = "black"
    window.add(ball)

    onmouseclicked(bouncing)


def bouncing(event):
    # bouncing function could use change global variables
    global GRAVITY, VY, ball, COUNT
    # if count more than constance GAME_OVER, the ball stops in the initial position
    if COUNT >= GAME_OVER:
        window.add(ball)

    else:
        # it means the ball is moving, so function do nothing
        if ball.x != START_X and ball.y != START_Y:
            pass

        else:
            while True:
                # simulate free fall and bounce motion
                GRAVITY += 1
                VY += GRAVITY
                ball.move(VX, VY)
                pause(DELAY)
                ball_y = ball.y+SIZE

                # if ball_y more than window.height, it means the ball touch floor
                if ball_y >= window.height:
                    VY = -VY*REDUCE
                    # Simulate bouncing ball motion
                    while True:
                        GRAVITY -= 1
                        VY = VY + GRAVITY
                        ball.move(VX, VY)
                        pause(DELAY)
                        # it means the ball bouncing to the top and start to falling
                        if GRAVITY == 0:
                            break
                # The ball move outside of window, put the ball back to the start location
                if ball.x+SIZE >= window.width:
                    window.remove(ball)
                    ball = GOval(SIZE, SIZE, x=30, y=40)
                    ball.filled = True
                    window.add(ball)
                    COUNT += 1
                    break

if __name__ == "__main__":
    main()
