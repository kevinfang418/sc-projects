"""
File: draw_line.py
Name: Kevin Fang
-------------------------
TODO:
"""
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Assign window as constant to create canvas
window = GWindow()
SIZE = 10
# a, b ,c ,d are global variables, so define them as 0 value
a = b = c = d = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(set_point)


def set_point(event):
    # a and b are global variables to store mouse event when everytime mouse clicked
    global a, b, c, d
    a = event.x
    b = event.y
    # check c and d are circle (object)
    maybe_circle = window.get_object_at(c, d)

    # draw circle when c and d are (0, 0)
    if c == d == 0:
        point = GOval(SIZE, SIZE, x=a-SIZE/2, y=b-SIZE/2)
        point.filled = False
        window.add(point)
        c = a
        d = b
    # if (c, d) is circle and not (0, 0), we need to draw a line from (c, d) to (a, b)
    elif maybe_circle is not None and c != d != 0:
        line = GLine(c, d, a, b)
        window.add(line)
        window.remove(maybe_circle)
        c = 0
        d = 0


if __name__ == "__main__":
    main()
