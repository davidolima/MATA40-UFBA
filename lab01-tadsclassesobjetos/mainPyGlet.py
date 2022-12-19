# ###############################################
# Visualiza um conjunto de pontos usando PyGlet #
# ###############################################

import sys
import random
from datetime       import datetime

import cCor
import cPontoColorido

import pyglet
from pyglet         import shapes
from pyglet.window  import Window
from pyglet.window  import key

WIN_X       = 800
WIN_Y       = 800
NUM_PTOS    = 20
MAX_Y       = 1000
OFFSET      = 10

# *******************************************************
# ***                                                 ***
# *******************************************************
def preencheVetor(v):

    deltaX  = WIN_X / NUM_PTOS

    for i in range(NUM_PTOS):
        corPto = cCor.cCor( random.randint(0, 255), 
                            random.randint(0, 255), 
                            random.randint(0, 255)  )
        v.append(cPontoColorido.cPontoCor(  i*deltaX+OFFSET,
                                            random.randint(0, MAX_Y), 
                                            corPto))

# *******************************************************
# ***                                                 ***
# *******************************************************
def montaListaDesenho(vet, formas):

    escalaY = WIN_Y / MAX_Y

    for i in range(NUM_PTOS):
        cor = vet[i].getCorPto()
        formas.append(shapes.Circle(  vet[i].getX(), vet[i].getY(), 2, color=(cor.getR(), cor.getG(), cor.getB()), batch=batch)) 

    formas.append(shapes.Line(OFFSET, OFFSET, OFFSET, WIN_Y, width=2, color=(255, 0 , 0), batch=batch))
    formas.append(shapes.Line(OFFSET, OFFSET, WIN_X, OFFSET, width=2, color=(0, 255 , 0), batch=batch))

# *******************************************************
# ***                                                 ***
# *******************************************************
def gameLoop(v):

    global window, batch

    window = pyglet.window.Window(WIN_X, WIN_Y)
    window.set_caption('Visualiza Algoritmo Min-Max')

    batch   = pyglet.graphics.Batch()
    formas = []

    montaListaDesenho(v, formas)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.app.run()


# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    v = [];

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if (len(sys.argv) > 1):
        NUM_PTOS = int(sys.argv[1])

    preencheVetor(v)

    gameLoop(v)
