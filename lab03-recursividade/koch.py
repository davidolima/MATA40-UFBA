import pyglet as pg
import numpy
from pyglet import shapes

MAX_LEVEL = 1

WIN_X = 500
WIN_Y = 500
OFFSET_X = WIN_X // 2
OFFSET_Y = WIN_Y // 2

def getTamanhoLinha(x,y,x1,y1):
    return ((x1-x)**2+(y1-y)**2)**0.5

def criarTriangulo(x,y,size):
    base = (x-size/2, y-size/2,
            x+size/2, y-size/2) 
    esq  = (x-size/2, y-size/2,
            x       , y+size/2)
    dir  = (x+size/2, y-size/2,
            x       , y+size/2)

    print("## Tamanhos ##")
    print("Base:",getTamanhoLinha(base[0],base[1],base[2],base[3]))
    print("Lado Esq:",getTamanhoLinha(esq[0],esq[1],esq[2],esq[3]))
    print("Lado Dir:",getTamanhoLinha(dir[0],dir[1],dir[2],dir[3]))

    d.append(shapes.Line(base[0],base[1],base[2],base[3],
                          width=5, batch=batch,color=(255,0,0)))
    d.append(shapes.Line(esq[0],esq[1],esq[2],esq[3],
                          width=5, batch=batch,color=(0,255,0)))
    d.append(shapes.Line(dir[0],dir[1],dir[2],dir[3],
                          width=5, batch=batch,color=(0,0,255)))
    
def criarFloco():
    d.clear()
    criarTriangulo(OFFSET_X,OFFSET_Y,100)

def desenharLinha(ks):
    return ks

if __name__ == '__main__':
    global window, batch, d
    window = pg.window.Window(WIN_X,WIN_Y)
    window.set_caption("Floco de Neve - David de Oliveira Lima")

    batch = pg.graphics.Batch()
    d = []

    criarFloco()

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pg.app.run()
