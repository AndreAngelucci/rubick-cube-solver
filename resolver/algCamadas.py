#algoritmo de camadas para resolucao do rubik cube
from rubik import *
from enums import *

class AlgoritmoCamadas:
    def __init__(self, cubo):
        #matrizes do cubo
        self.cubo = cubo

    def movePeca(self, faceOrigem, origem, faceDestino, destino):
        print "x"

    def cruzBranca(self):
        #encontra a face amarela para fazer a cruz
        faceAmarela = cubo.procuraCor(Cor.amarelo)
        #encontra os meios brancos e faz a cruz
        while (True):
            meioBranco = []
            for indexFace in range(0, 6):
                faceAnalise = cubo.retornaFace(Faces[indexFace])
                for i in range(0, 3):
                    #pega os meios da face
                    if (i == 0):
                        meio = [1][0]
                    elif (i == 1):
                        meio = [0][1]
                    elif (i == 2):
                        meio = [1][1]
                    else:
                        meio = [2][1]
                    #verifica se eh branca
                    if (faceAnalise[meio[0]][meio[1]] == Cor.branca):
                        faceMeioBranco = Faces[indexFace]
                        meioBranco = meio
                        break
                break
            #move a peca para o destino
        #verifica o destino da peca
        destino = []
        if (faceAmarela[1][0] != Cores.branco):
            destino = [1][0]
        elif (faceAmarela[0][1] != Cores.branco):
            destino = [0][1]
        elif (faceAmarela[1][1] != Cores.branco):
            destino = [1][1]
        elif (faceAmarela[2][1] != Cores.branco):
            destino = [2][1]
        movePeca(
            faceMeioBranco, meioBranco,
            faceAmarela, destino
        )
        

    def resolver():
        #resolve
        cruzBranca()