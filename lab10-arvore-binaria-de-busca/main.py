# Lab09 - Árvore Binária 

import cNo
import cABB

import sys
import random
import math
from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

  random.seed(int(datetime.now().strftime('%H%M%S')))

  n = 20
  if (len(sys.argv) > 1):
      n = int(sys.argv[1])
      if n < 0:
          n = 20

  arvore = cABB.cABB()

  for i in range(n):
    chave   = random.randint(0, 1000)
    arvore.insereChave(chave)

  # print("Percurso em Pré-Ordem:")
  # print("======================")
  # arvore.percorreArvore(cABB.percursos.PRE_ORDEM)
  # print("======================")

  print("Percurso em In-Ordem:")
  print("======================")
  arvore.percorreArvore(cABB.percursos.IN_ORDEM)
  print("======================")

  # print("Percurso em Post-Ordem:")
  # print("======================")
  # arvore.percorreArvore(cABB.percursos.POST_ORDEM)
  # print("======================")
