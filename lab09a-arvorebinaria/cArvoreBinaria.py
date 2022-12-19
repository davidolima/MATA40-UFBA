# ##################################################
# Classe cArvore de define uma Árvore Binária
# ##################################################

import cNo

# *******************************************************
#
# *******************************************************
class percursos:
  PRE_ORDEM   = 0
  IN_ORDEM    = 1
  POST_ORDEM  = 2

# *******************************************************
#
# *******************************************************
class cArvoreBinaria:
  
  chave = 0

# *******************************************************
  def __init__(self, n):
    self.__raiz__   = None
    self.__numNos__ = 0

    self.__raiz__   = self.__MontaAB__(n)

# *******************************************************
  def getNumNos(self):
    return self.__numNos__

# *******************************************************
  def percorreArvore(self, percurso=percursos.PRE_ORDEM):

    if percurso == percursos.PRE_ORDEM:
      self.__preOrdem__(self.__raiz__)

    elif percurso == percursos.IN_ORDEM:
      self.__inOrdem__(self.__raiz__)

    elif percurso == percursos.POST_ORDEM:
      self.__postOrdem__(self.__raiz__)
 
# *******************************************************
  def __MontaAB__(self, n):

    if n == 0:
      return None;

    novoNo = cNo.cNo(self.chave);
    self.chave += 1 

    if novoNo == None:
      return novoNo

    self.__numNos__ += 1

    nnd = n // 2
    nne = n - nnd - 1

    novoNo.setFilhoEsq(self.__MontaAB__(nne))
    novoNo.setFilhoDir(self.__MontaAB__(nnd))

    return novoNo
 
# *******************************************************
  def __preOrdem__(self, raiz):
 
    if raiz is None:
      print(".")

    else:
      print(raiz.getDado())
      self.__preOrdem__(raiz.getFilhoEsq())
      self.__preOrdem__(raiz.getFilhoDir())

 
# *******************************************************
  def __inOrdem__(self, raiz):
 
    if raiz is None:
      print(".")

    else:
      self.__inOrdem__(raiz.getFilhoEsq())
      print(raiz.getDado())
      self.__inOrdem__(raiz.getFilhoDir())

 
# *******************************************************
  def __postOrdem__(self, raiz):
 
    if raiz is None:
      print(".")

    else:
      self.__postOrdem__(raiz.getFilhoEsq())
      self.__postOrdem__(raiz.getFilhoDir())
      print(raiz.getDado())

