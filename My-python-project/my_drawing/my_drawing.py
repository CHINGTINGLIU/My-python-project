"""
File: my_drawing.py
Name: Alice Liu
----------------------
"""

from campy.graphics.gobjects import GOval, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My favorite 'LinaBell'

    This is my favorite figure in the Disney!
    She is a cutie fox, who can solve many problem when she encounters,
    so I want to learn Python so that someday in the future I can be like her.
    """
    window = GWindow(width=800, height=800, title='LinaBell')
    # --- Background Circle ---
    bg = GOval(500, 500, x=150, y=150)
    bg.filled = True
    bg.fill_color = '#E4A29B'  # warm rose-pink
    bg.color = '#E4A29B'
    window.add(bg)
    # --- Tail (behind head) ---
    tail_arc = GArc(380, 380, 80, 130, x=460, y=220)  #
    tail_arc.filled = True
    tail_arc.fill_color = 'pink'
    tail_arc.color = 'plum'
    window.add(tail_arc)
    tail_arc2 = GArc(380, 380, 80, 90, x=465, y=220)  #
    tail_arc2.filled = True
    tail_arc2.fill_color = 'peachpuff'
    tail_arc2.color = 'plum'
    window.add(tail_arc2)
    # --- Ears ---
    l_ear_arc = GArc(280, 280, 130, 180, x=200, y=230)  #
    l_ear_arc.filled = True
    l_ear_arc.fill_color = 'pink'
    l_ear_arc.color = 'plum'
    window.add(l_ear_arc)
    l_ear_arc2 = GArc(200, 200, 130, 180, x=210, y=260)  #
    l_ear_arc2.filled = True
    l_ear_arc2.fill_color = 'peachpuff'
    l_ear_arc2.color = 'plum'
    window.add(l_ear_arc2)
    r_ear_arc = GArc(300, 300, 30, 100, x=450, y=350)  #
    r_ear_arc.filled = True
    r_ear_arc.fill_color = 'pink'
    r_ear_arc.color = 'plum'
    window.add(r_ear_arc)
    r_ear_arc2 = GArc(200, 200, 30, 100, x=500, y=360)  #
    r_ear_arc2.filled = True
    r_ear_arc2.fill_color = 'peachpuff'
    r_ear_arc2.color = 'plum'
    window.add(r_ear_arc2)
    # --- Head ---
    arc = GArc(400, 800, 0, 180, x=200, y=300)  #
    arc.filled = True
    arc.fill_color = 'pink'
    arc.color = 'plum'
    window.add(arc)
    # --- Eyes ---
    l_periphery_oval = GOval(100, 100, x=280, y=350)  #
    l_periphery_oval.filled = True
    l_periphery_oval.fill_color = 'peachpuff'
    l_periphery_oval.color = 'plum'
    window.add(l_periphery_oval)
    l_eye_oval = GOval(50, 50, x=310, y=390)  #
    l_eye_oval.filled = True
    l_eye_oval.fill_color = 'steelblue'
    window.add(l_eye_oval)
    l_eye_oval2 = GOval(35, 35, x=320, y=400)  #
    l_eye_oval2.filled = True
    l_eye_oval2.fill_color = 'black'
    window.add(l_eye_oval2)
    l_eye_oval3 = GOval(15, 15, x=340, y=400)  #
    l_eye_oval3.filled = True
    l_eye_oval3.fill_color = 'white'
    window.add(l_eye_oval3)
    r_periphery_oval = GOval(100, 100, x=420, y=350)  #
    r_periphery_oval.filled = True
    r_periphery_oval.fill_color = 'peachpuff'
    r_periphery_oval.color = 'plum'
    window.add(r_periphery_oval)
    r_eye_oval = GOval(50, 50, x=440, y=390)  #
    r_eye_oval.filled = True
    r_eye_oval.fill_color = 'steelblue'
    window.add(r_eye_oval)
    r_eye_oval2 = GOval(35, 35, x=440, y=400)  #
    r_eye_oval2.filled = True
    r_eye_oval2.fill_color = 'black'
    window.add(r_eye_oval2)
    r_eye_oval3 = GOval(15, 15, x=460, y=400)  #
    r_eye_oval3.filled = True
    r_eye_oval3.fill_color = 'white'
    window.add(r_eye_oval3)
    # --- Mouth area ---
    mouth_oval = GOval(100, 85, x=350, y=410)  #
    mouth_oval.filled = True
    mouth_oval.fill_color = 'peachpuff'
    mouth_oval.color = 'plum'
    window.add(mouth_oval)
    mouth_oval2 = GOval(30, 20, x=385, y=430)  #
    mouth_oval2.filled = True
    mouth_oval2.fill_color = 'pink'
    mouth_oval2.color = 'rosybrown'
    window.add(mouth_oval2)
    # --- Paws ---
    l_paw_oval = GOval(110, 90, x=190, y=430)  #
    l_paw_oval.filled = True
    l_paw_oval.fill_color = 'pink'
    l_paw_oval.color = 'plum'
    window.add(l_paw_oval)
    r_paw_oval = GOval(110, 90, x=500, y=430)  #
    r_paw_oval.filled = True
    r_paw_oval.fill_color = 'pink'
    r_paw_oval.color = 'plum'
    window.add(r_paw_oval)
    # --- Blush ---
    l_blush_oval = GOval(70, 20, x=280, y=440)  #
    l_blush_oval.filled = True
    l_blush_oval.fill_color = 'salmon'
    l_blush_oval.color = 'plum'
    window.add(l_blush_oval)
    r_blush_oval = GOval(70, 20, x=450, y=440)  #
    r_blush_oval.filled = True
    r_blush_oval.fill_color = 'salmon'
    r_blush_oval.color = 'plum'
    window.add(r_blush_oval)
    # --- Flower on left ear ---
    for i in range(5):
        petal = GArc(200, 200, 72 * i, 50, x=250, y=280)
        petal.filled = True
        petal.fill_color = 'mediumpurple'
        petal.color = 'purple'
        window.add(petal)
    flower_center = GOval(30, 30, x=280, y=300)
    flower_center.filled = True
    flower_center.fill_color = 'gold'
    flower_center.color = 'goldenrod'
    window.add(flower_center)
    # --- Eyelashes  ---
    window.add(GLine(325, 395, 315, 390))
    window.add(GLine(345, 395, 355, 390))
    window.add(GLine(460, 395, 470, 390))
    window.add(GLine(480, 395, 490, 390))
    # --- 嘴部 (微笑線) ---
    window.add(GLine(402, 440, 402, 455))
    window.add(GLine(402, 455, 390, 465))
    window.add(GLine(402, 455, 414, 465))

    label = GLabel('CHINGTING LITTLE FOX: )', x=120, y=120)
    label.font = '-40'
    label.color = 'peru'
    window.add(label)


if __name__ == '__main__':
    main()
