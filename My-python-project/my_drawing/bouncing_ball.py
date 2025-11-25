"""
File: bouncing_ball.py
Name: Alice Liu
-------------------------
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variables
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
window = GWindow(800, 500, title='bouncing_ball.py')
total = 0
can_run = True
round_label = None


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global round_label
    ball.filled = True
    window.add(ball)
    round_label = GLabel("Round 0/ 3")
    round_label.font = "-30"
    round_label.color = "salmon"
    window.add(round_label, x=300, y=50)
    onmouseclicked(move_ball)


def move_ball(event):
    global total, can_run
    vy = 0
    if not can_run:
        return
    if total >= 3:
        return
    # if can_run is True:
    can_run = False
    while ball.x + SIZE <= window.width:

        can_run = False
        ball.move(VX, vy)

        if ball.y + SIZE <= window.height:
            vy += GRAVITY
        else:
            ball.y = window.height - SIZE
            vy = -vy * REDUCE
        pause(DELAY)

    total += 1
    window.remove(ball)
    round_label.text = f"Round {total} / 3"
    window.add(ball, x=START_X, y=START_Y)
    can_run = True


if __name__ == "__main__":
    main()
