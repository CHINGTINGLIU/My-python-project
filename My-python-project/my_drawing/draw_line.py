"""
File: draw_line.py
Name: Alice Liu
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 30  # This constant controls the size of the hole
# Global variable
window = GWindow()
circle = GOval(SIZE, SIZE)
can_line = False
start_x = 0
start_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    This function draws a hollow circle centered the mouse when it cannot line,
    , and it draws a line after drawing a hollow circle.
    """
    global can_line, circle, start_x, start_y
    if not can_line:
        window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        start_x = mouse.x
        start_y = mouse.y
        can_line = True
    else:
        window.remove(circle)
        line = GLine(start_x, start_y, mouse.x, mouse.y)
        window.add(line)
        can_line = False   


if __name__ == "__main__":
    main()

