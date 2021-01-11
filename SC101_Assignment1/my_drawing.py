"""
File: my_drawing.py
Name: Kevin Fang
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    w = GWindow(800, 600, title='Golden Gate Bridge')

    floor1_central = GRect(300, 10, x=250, y=400)
    floor1_central.filled = True
    floor1_central.color = 'red'
    floor1_central.fill_color = 'red'
    w.add(floor1_central)

    floor1_1_central = GRect(120, 10, x=85, y=400)
    floor1_1_central.filled = True
    floor1_1_central.color = 'red'
    floor1_1_central.fill_color = 'red'
    w.add(floor1_1_central)

    floor1_2_central = GRect(120, 10, x=85, y=420)
    floor1_2_central.filled = True
    floor1_2_central.color = 'red'
    floor1_2_central.fill_color = 'red'
    w.add(floor1_2_central)

    floor2_central = GRect(300, 10, x=250, y=420)
    floor2_central.filled = True
    floor2_central.color = 'red'
    floor2_central.fill_color = 'red'
    w.add(floor2_central)

    floor2_1_central = GRect(120, 10, x=588, y=400)
    floor2_1_central.filled = True
    floor2_1_central.color = 'red'
    floor2_1_central.fill_color = 'red'
    w.add(floor2_1_central)

    floor2_2_central = GRect(120, 10, x=588, y=420)
    floor2_2_central.filled = True
    floor2_2_central.color = 'red'
    floor2_2_central.fill_color = 'red'
    w.add(floor2_2_central)

    arc_central = GOval(290, 300, x=250, y=80)
    arc_central.filled = True
    arc_central.fill_color = 'red'
    arc_central.color = 'red'
    w.add(arc_central)

    arc1_central = GOval(290, 300, x=250, y=70)
    arc1_central.filled = True
    arc1_central.color = 'white'
    arc1_central.fill_color = 'white'
    w.add(arc1_central)

    column1 = GRect(15, 300, x=220, y=190)
    column1.filled = True
    column1.color = 'darkred'
    column1.fill_color = 'darkred'
    w.add(column1)

    column1_1 = GRect(10, 80, x=255, y=310)
    column1_1.filled = True
    column1_1.color = 'red'
    column1_1.fill_color = 'red'
    w.add(column1_1)

    column1_2 = GRect(10, 60, x=275, y=330)
    column1_2.filled = True
    column1_2.color = 'red'
    column1_2.fill_color = 'red'
    w.add(column1_2)

    column1_3 = GRect(10, 40, x=295, y=350)
    column1_3.filled = True
    column1_3.color = 'red'
    column1_3.fill_color = 'red'
    w.add(column1_3)

    column1_4 = GRect(10, 20, x=315, y=370)
    column1_4.filled = True
    column1_4.color = 'red'
    column1_4.fill_color = 'red'
    w.add(column1_4)

    column1_5 = GRect(10, 10, x=335, y=380)
    column1_5.filled = True
    column1_5.color = 'red'
    column1_5.fill_color = 'red'
    w.add(column1_5)

    column1_6 = GRect(10, 5, x=355, y=385)
    column1_6.filled = True
    column1_6.color = 'red'
    column1_6.fill_color = 'red'
    w.add(column1_6)

    column1_7 = GRect(10, 5, x=375, y=385)
    column1_7.filled = True
    column1_7.color = 'red'
    column1_7.fill_color = 'red'
    w.add(column1_7)

    head1 = GRect(7, 25, x=224, y=165)
    head1.filled = True
    head1.color = 'darkred'
    head1.fill_color = 'darkred'
    w.add(head1)

    column2 = GRect(15, 300, x=560, y=190)
    column2.filled = True
    column2.color = 'darkred'
    column2.fill_color = 'darkred'
    w.add(column2)

    column2_1 = GRect(10, 80, x=535, y=310)
    column2_1.filled = True
    column2_1.color = 'red'
    column2_1.fill_color = 'red'
    w.add(column2_1)

    column2_2 = GRect(10, 60, x=515, y=330)
    column2_2.filled = True
    column2_2.color = 'red'
    column2_2.fill_color = 'red'
    w.add(column2_2)

    column2_3 = GRect(10, 40, x=495, y=350)
    column2_3.filled = True
    column2_3.color = 'red'
    column2_3.fill_color = 'red'
    w.add(column2_3)

    column2_4 = GRect(10, 20, x=475, y=370)
    column2_4.filled = True
    column2_4.color = 'red'
    column2_4.fill_color = 'red'
    w.add(column2_4)

    column2_5 = GRect(10, 10, x=455, y=380)
    column2_5.filled = True
    column2_5.color = 'red'
    column2_5.fill_color = 'red'
    w.add(column2_5)

    column2_6 = GRect(10, 5, x=435, y=385)
    column2_6.filled = True
    column2_6.color = 'red'
    column2_6.fill_color = 'red'
    w.add(column2_6)

    column2_7 = GRect(10, 5, x=415, y=385)
    column2_7.filled = True
    column2_7.color = 'red'
    column2_7.fill_color = 'red'
    w.add(column2_7)

    head2 = GRect(7, 25, x=564, y=165)
    head2.filled = True
    head2.color = 'darkred'
    head2.fill_color = 'darkred'
    w.add(head2)

    feet1 = GRect(30, 15, x=213, y=480)
    feet1.filled = True
    feet1.color = 'darkred'
    feet1.fill_color = 'darkred'
    w.add(feet1)

    feet2 = GRect(30, 15, x=552, y=480)
    feet2.filled = True
    feet2.color = 'darkred'
    feet2.fill_color = 'darkred'
    w.add(feet2)

    arc_left = GArc(500, 600, 0, -90, x=-40, y=80)
    arc_left.filled = False
    arc_left.color = "red"
    w.add(arc_left)

    column1_1_left = GRect(10, 70, x=190, y=320)
    column1_1_left.filled = True
    column1_1_left.color = 'red'
    column1_1_left.fill_color = 'red'
    w.add(column1_1_left)

    column1_2_left = GRect(10, 45, x=170, y=345)
    column1_2_left.filled = True
    column1_2_left.color = 'red'
    column1_2_left.fill_color = 'red'
    w.add(column1_2_left)

    column1_3_left = GRect(10, 20, x=150, y=370)
    column1_3_left.filled = True
    column1_3_left.color = 'red'
    column1_3_left.fill_color = 'red'
    w.add(column1_3_left)

    column1_4_left = GRect(10, 5, x=130, y=385)
    column1_4_left.filled = True
    column1_4_left.color = 'red'
    column1_4_left.fill_color = 'red'
    w.add(column1_4_left)

    arc_right = GArc(500, 600, 180, 90, x=585, y=80)
    arc_right.filled = False
    arc_right.color = "red"
    w.add(arc_right)

    column1_1_right = GRect(10, 70, x=595, y=320)
    column1_1_right.filled = True
    column1_1_right.color = 'red'
    column1_1_right.fill_color = 'red'
    w.add(column1_1_right)

    column1_2_right = GRect(10, 45, x=615, y=345)
    column1_2_right.filled = True
    column1_2_right.color = 'red'
    column1_2_right.fill_color = 'red'
    w.add(column1_2_right)

    column1_3_right = GRect(10, 20, x=635, y=370)
    column1_3_right.filled = True
    column1_3_right.color = 'red'
    column1_3_right.fill_color = 'red'
    w.add(column1_3_right)

    column1_4_right = GRect(10, 5, x=655, y=385)
    column1_4_right.filled = True
    column1_4_right.color = 'red'
    column1_4_right.fill_color = 'red'
    w.add(column1_4_right)

    label = GLabel("San Francisco", 170, 150)
    label.font = '-80'
    label.color = 'red'
    w.add(label)

    label1 = GLabel("StanCode SC101 Nov | Kevin", 510, 550)
    label1.font = '-20'
    label1.color = 'red'
    w.add(label1)

if __name__ == '__main__':
    main()
