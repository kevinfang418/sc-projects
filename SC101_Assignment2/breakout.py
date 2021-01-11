"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3
graphics = BreakoutGraphics()


def main():
    graphics.lives_table.font = '-30'
    graphics.window.add(graphics.lives_table, graphics.window.width-graphics.lives_table.width, graphics.window.height)
    graphics.window.add(graphics.score_table, 0, graphics.window.height)
    onmouseclicked(start_game)


def start_game(event):
    global NUM_LIVES
    if NUM_LIVES <= 0:
        graphics.reset_ball()
    elif graphics.ball.x != (graphics.window.width - graphics.ball.width) / 2 \
            and graphics.ball.y != (graphics.window.height - graphics.ball.height) / 2:
        pass

    else:
        graphics.start(event)
        graphics.ball_velocity()

        while True:
            pause(FRAME_RATE)
            if graphics.ball.y >= graphics.window.height:
                NUM_LIVES -= 1
                graphics.lives_table.text = "Lives: "+str(NUM_LIVES)
                graphics.window.remove(graphics.ball)
                graphics.reset_ball()
                break

            graphics.ball.move(graphics.dx, graphics.dy)
            graphics.ball_touch_something()
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.dx = -graphics.dx
            elif graphics.ball.y <= 0:
                graphics.dy = -graphics.dy
            elif graphics.total_bricks == 0:

                break

        graphics.reset_ball()

if __name__ == '__main__':
    main()
