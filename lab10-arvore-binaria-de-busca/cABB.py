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
class cABB:
  
# *******************************************************
  def __init__(self):
    self.__raiz__   = None
    self.__numNos__ = 0


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
  def insereChave(self, k):

    self.__raiz__ = self.__insereChave__(self.__raiz__, k)

 
# *******************************************************
  def buscaChave(self, k):

    return self.__buscaChave__(self.__raiz__, k)
 
# *******************************************************
  def removeChave(self, k):

    return self.__removeChave__(self.__raiz__, k)
 
# *******************************************************
  def __insereChave__(self, raiz: cNo.cNo, k):
    if raiz is None:
      return cNo.cNo(k)

    if raiz.getDado() > k:
      self.__numNos__ += 1
      raiz.setFilhoEsq(self.__insereChave__(raiz.getFilhoEsq(), k))
    else:
      self.__numNos__ += 1
      raiz.setFilhoDir(self.__insereChave__(raiz.getFilhoDir(), k))

    return raiz
            
# *******************************************************
  def __buscaChave__(self, raiz, k):
    if raiz is None:
      return
    elif raiz.getDado() == k:
      return True

    if raiz.getDado() > k:
      return self.__buscaChave__(raiz.getFilhoEsq(), k)
    else:
      return self.__buscaChave__(raiz.getFilhoDir(), k)

    return raiz
 
# *******************************************************
  def __removeChave__(self, raiz, k):

    return False
 
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