"""
File: breakout.py
Name: Alice Liu
------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program plays a Python game 'breakout'. A ball will be bouncing around the GWindow
Players if the user click the mouse for the 1st time each round, and it will end at
if there is no more lives or bricks.
"""
from campy.graphics.gobjects import GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!

    while True:
        # getter
        vx = graphics.get_dx()      # 那如果不放在迴圈外的原因是什麼--因為球速會在遊戲過程中改變（碰牆、碰板、碰磚），若放在外面只會讀取一次，後續的反彈就不會更新。
        vy = graphics.get_dy()
        graphics.ball.move(vx, vy)
        pause(FRAME_RATE)
        graphics.ball_collide_objects()
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            graphics.set_dx()
        elif graphics.ball.y <= 0:
            graphics.set_dy()
        elif graphics.ball.y + graphics.ball.height > graphics.window.height:
            lives -= 1
            graphics.reset_ball()
        if graphics.brick_count == 0:
            label = GLabel("You Win!", x=120, y=300)
            label.font = '-40'
            label.color = 'salmon'
            graphics.window.add(label)
            break
        if lives == 0:
            label = GLabel('Game Over.', x=120, y=300)
            label.font = '-40'
            label.color = 'salmon'
            graphics.window.add(label)
            break


if __name__ == '__main__':
    main()



