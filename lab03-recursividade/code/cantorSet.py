# ###############################################
# Desenha o conjunto de Cantor
# ###############################################

import sys
from datetime       import datetime

import pyglet
from pyglet         import shapes
from pyglet.window  import Window
from pyglet.window  import key

WIN_X       = 1000
WIN_Y       = 400
OFFSET_X    = WIN_X // 20

# *******************************************************
# ***                                                 ***
# *******************************************************
def criaCantorSet(cs):

    cs.clear()

    cs.append(shapes.Line(OFFSET_X, OFFSET_Y, WIN_X - OFFSET_X, OFFSET_Y, width=2, batch=batch))

    desenhaCurva(cs, OFFSET_X, OFFSET_Y, WIN_X - OFFSET_X, OFFSET_Y, 0)

# *******************************************************
# ***                                                 ***
# *******************************************************
def desenhaCurva(forma, xi, yi, xf, yf, level):

    if level == MAX_LEVEL:
        forma.append(shapes.Line( xi, yi, xf, yf, width=5, batch=batch))
    else:
        t = 1 / 3;
        x0 = int(xi * (1 - t) + xf * t)

        t = 2 / 3;
        x1 = int(xi * (1 - t) + xf * t)

        y = yi + OFFSET_Y

        forma.append(shapes.Line( xi, y, x0, y, width=5, batch=batch))
        desenhaCurva(forma, xi, y, x0, y, level+1)

        forma.append(shapes.Line( x1, y, xf, y, width=5, batch=batch))
        desenhaCurva(forma, x1, y, xf, y, level+1) 

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    global window, batch, MAX_LEVEL, OFFSET_Y, OFFSET_COR

    if (len(sys.argv) > 1):
        MAX_LEVEL = int(sys.argv[1])
    else:
        MAX_LEVEL = 2

    OFFSET_Y    = WIN_Y // (MAX_LEVEL + 2)

    window = pyglet.window.Window(WIN_X, WIN_Y)
    window.set_caption('Desenha Cantor Set')

    batch = pyglet.graphics.Batch()
    desenho = []

    criaCantorSet(desenho)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.app.run()
