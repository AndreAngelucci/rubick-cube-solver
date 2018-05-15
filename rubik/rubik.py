import numpy as np
from util.enums import *
from util.operacoesMatriz import *
from copy import copy

#associacao entre movimento e face
class Movimento():
    def __init__(self, face, sentido, giros = 1):
        if (giros < 1):
            raise Exception("Quantidade de giros invalida")
        self.face = face
        self.sentido = sentido
        self.giros = giros

#abstracao do cubo magico
class Rubik():
    #movimentos padroes
    fh = Movimento(Faces.frente, SentidoMovimento.horario)    
    fhDuplo = Movimento(Faces.frente, SentidoMovimento.horario, 2)
    fa = Movimento(Faces.frente, SentidoMovimento.antiHorario)
    faDuplo = Movimento(Faces.frente, SentidoMovimento.antiHorario, 2)
    sh = Movimento(Faces.superior, SentidoMovimento.horario)
    shDuplo = Movimento(Faces.superior, SentidoMovimento.horario, 2)
    sa = Movimento(Faces.superior, SentidoMovimento.antiHorario)    
    saDuplo = Movimento(Faces.superior, SentidoMovimento.antiHorario, 2)
    dh = Movimento(Faces.direita, SentidoMovimento.horario)
    dhDuplo = Movimento(Faces.direita, SentidoMovimento.horario, 2)
    da = Movimento(Faces.direita, SentidoMovimento.antiHorario)
    daDuplo = Movimento(Faces.direita, SentidoMovimento.antiHorario, 2)
    eh = Movimento(Faces.esquerda, SentidoMovimento.horario)
    ehDuplo = Movimento(Faces.esquerda, SentidoMovimento.horario, 2)
    ea = Movimento(Faces.esquerda, SentidoMovimento.antiHorario)
    eaDuplo = Movimento(Faces.esquerda, SentidoMovimento.antiHorario, 2)
    ih = Movimento(Faces.inferior, SentidoMovimento.horario)
    ihDuplo = Movimento(Faces.inferior, SentidoMovimento.horario, 2)
    ia = Movimento(Faces.inferior, SentidoMovimento.antiHorario)
    iaDuplo = Movimento(Faces.inferior, SentidoMovimento.antiHorario, 2)
    ch = Movimento(Faces.costas, SentidoMovimento.horario)
    chDuplo = Movimento(Faces.costas, SentidoMovimento.horario, 2)
    ca = Movimento(Faces.costas, SentidoMovimento.antiHorario)
    caDuplo = Movimento(Faces.costas, SentidoMovimento.antiHorario, 2)    

    def __init__(self, frente = [], superior = [], direita = [], esquerda = [], inferior = [], costas = []):
        #classe que abstrai o cubo magico.        
        self.faceFrente = frente if frente != [] else matrizCorVazia()
        self.faceSuperior = superior if superior != [] else matrizCorVazia()
        self.faceDireita = direita if direita != [] else matrizCorVazia()
        self.faceEsquerda = esquerda if esquerda != [] else matrizCorVazia()
        self.faceInferior = inferior if inferior != [] else matrizCorVazia()
        self.faceCostas = costas if costas != [] else matrizCorVazia()

    #retorna qual a face de determinada cor
    def procuraFace(self, cor):
        if (self.faceFrente[1][1] == cor):
            return Faces.frente
        elif (self.faceSuperior[1][1] == cor):
            return Faces.superior
        elif (self.faceDireita[1][1] == cor):
            return Faces.direita
        elif (self.faceEsquerda[1][1] == cor):
            return Faces.esquerda
        elif (self.faceInferior[1][1] == cor):
            return Faces.inferior
        elif (self.faceCostas[1][1] == cor):
            return Faces.costas

    def tipoPeca(self, linha, coluna):
        #retorna qual o tipo da peca
        if ((linha == 1) and (coluna == 1)):
            return Pecas.central
        elif ((coluna == 1) or (linha == 1)):
            return Pecas.meio
        else:
            return Pecas.lateral
    
    #recebe uma face e retorna a matriz
    def retornaFace(self, face):
        if (face == Faces.frente):
            return self.faceFrente
        elif (face == Faces.direita):
            return self.faceDireita
        elif (face == Faces.esquerda):
            return self.faceEsquerda
        elif (face == Faces.superior):
            return self.faceSuperior
        elif (face == Faces.inferior):
            return self.faceInferior
        elif (face == Faces.costas):
            return self.faceCostas
        else:
            raise Exception("Face invalida")


    def representacaoGrafica(self):
        #mostra na tela uma representacao atual do cubo
        print('')
        for x in range(0, 3):	
            print('#        '+ str(self.faceSuperior[x][0].value)+ ' '+ str(self.faceSuperior[x][1].value)+ ' '+ str(self.faceSuperior[x][2].value))
        print('#')
        for x in range(0, 3):	
            print('# '+ 
                str(self.faceEsquerda[x][0].value)+ ' '+ str(self.faceEsquerda[x][1].value)+ ' '+ str(self.faceEsquerda[x][2].value)+ '  '+
                str(self.faceFrente[x][0].value)+ ' '+ str(self.faceFrente[x][1].value)+ ' '+ str(self.faceFrente[x][2].value)+ '  '+
                str(self.faceDireita[x][0].value)+ ' '+ str(self.faceDireita[x][1].value)+ ' '+ str(self.faceDireita[x][2].value)+ '  '+
                str(self.faceCostas[x][0].value)+ ' '+ str(self.faceCostas[x][1].value)+ ' '+ str(self.faceCostas[x][2].value)+ '  '
            )
        print('#')
        for x in range(0, 3):	
            print('#        '+ str(self.faceInferior[x][0].value)+ ' '+ str(self.faceInferior[x][1].value)+ ' '+ str(self.faceInferior[x][2].value))
        print('')    

    def mover(self, movimento):
        #identifa a face que sera movimentada
        #e seus vizinhos
        if (movimento.face == Faces.frente):
            faceMovimentar = self.faceFrente
        elif (movimento.face == Faces.superior):
            faceMovimentar = self.faceSuperior
        elif (movimento.face == Faces.direita):
            faceMovimentar = self.faceDireita
        elif (movimento.face == Faces.esquerda):
            faceMovimentar = self.faceEsquerda
        elif (movimento.face == Faces.inferior):
            faceMovimentar = self.faceInferior
        elif (movimento.face == Faces.costas):
            faceMovimentar = self.faceCostas
        else:
            raise Exception("Face invalida.")            
        #move a face escolhida em 90 graus
        #horario ou anti-horario        
        matrizAux = np.rot90(
            faceMovimentar, 
            (1 if movimento.sentido == SentidoMovimento.antiHorario else (-1)) * movimento.giros
        ).tolist()
        #coloca a matriz rotacionada na face que ira ser movimentada
        for x in range(0, 3):
            for y in range(0, 3):
                faceMovimentar[x][y] = matrizAux[x][y]
        #movimento das faces vizinhas
        for rotacoes in range(0, movimento.giros):
            if ((movimento.face == Faces.frente and movimento.sentido == SentidoMovimento.horario) or (movimento.face == Faces.costas and movimento.sentido == SentidoMovimento.antiHorario)):
                #frente horario e costas anti-horario
                b = movimento.face == Faces.frente
                aux1 = np.copy(self.faceSuperior[:])
                colunaParaLinha(self.faceEsquerda, self.faceSuperior, (2 if b else 0), (2 if b else 0), True)
                aux2 = np.copy(self.faceDireita[:])
                linhaParaColuna(aux1, self.faceDireita, (2 if b else 0), (0 if b else 2), False)
                aux1 = np.copy(self.faceInferior[:])
                colunaParaLinha(aux2, self.faceInferior, (0 if b else 2), (0 if b else 2), True)
                linhaParaColuna(aux1, self.faceEsquerda, (0 if b else 2), (2 if b else 0), False)
            elif ((movimento.face == Faces.frente and movimento.sentido == SentidoMovimento.antiHorario) or (movimento.face == Faces.costas and movimento.sentido == SentidoMovimento.horario)):
                #frente anti-horario e costas horario
                b = movimento.face == Faces.frente
                aux1 = np.copy(self.faceSuperior[:])
                colunaParaLinha(self.faceDireita, self.faceSuperior, (0 if b else 2), (2 if b else 0), False)
                aux2 = np.copy(self.faceEsquerda[:])
                linhaParaColuna(aux1, self.faceEsquerda, (2 if b else 0), (2 if b else 0), True)
                aux1 = np.copy(self.faceInferior[:])
                colunaParaLinha(aux2, self.faceInferior, (2 if b else 0), (0 if b else 2), False)
                linhaParaColuna(aux1, self.faceDireita, (0 if b else 2), (0 if b else 2), True)                    
            elif ((movimento.face == Faces.superior and movimento.sentido == SentidoMovimento.horario) or (movimento.face == Faces.inferior and movimento.sentido == SentidoMovimento.antiHorario)):
                #superior horario e inferior anti-horario
                linhaOrigem = (0 if movimento.face == Faces.superior else 2)
                aux1 = np.copy(self.faceEsquerda[:])
                linhaParaLinha(self.faceFrente, self.faceEsquerda, linhaOrigem, linhaOrigem, False)
                aux2 = np.copy(self.faceCostas[:])
                linhaParaLinha(aux1, self.faceCostas, linhaOrigem, linhaOrigem, False)
                aux1 = np.copy(self.faceDireita[:])
                linhaParaLinha(aux2, self.faceDireita, linhaOrigem, linhaOrigem, False)
                linhaParaLinha(aux1, self.faceFrente, linhaOrigem, linhaOrigem, False)
            elif ((movimento.face == Faces.superior and movimento.sentido == SentidoMovimento.antiHorario) or (movimento.face == Faces.inferior and movimento.sentido == SentidoMovimento.horario)):
                #superior anti-horario e inferior horario
                linhaOrigem = (0 if movimento.face == Faces.superior else 2)
                aux1 = np.copy(self.faceFrente[:])
                linhaParaLinha(self.faceEsquerda, self.faceFrente, linhaOrigem, linhaOrigem, False)
                aux2 = np.copy(self.faceDireita[:])
                linhaParaLinha(aux1, self.faceDireita, linhaOrigem, linhaOrigem, False)
                aux1 = np.copy(self.faceCostas[:])
                linhaParaLinha(aux2, self.faceCostas, linhaOrigem, linhaOrigem, False)
                linhaParaLinha(aux1, self.faceEsquerda, linhaOrigem, linhaOrigem, False)
            elif ((movimento.face == Faces.esquerda and movimento.sentido == SentidoMovimento.horario) or (movimento.face == Faces.direita and movimento.sentido == SentidoMovimento.antiHorario)):
                #esquerda horario e direita anti-horario
                colOrigem = (0 if movimento.face == Faces.esquerda else 2)
                aux1 = np.copy(self.faceFrente[:])
                colunaParaColuna(self.faceSuperior, self.faceFrente, colOrigem, colOrigem, False)
                aux2 = np.copy(self.faceInferior[:])
                colunaParaColuna(aux1, self.faceInferior, colOrigem, colOrigem, False)
                aux1 = np.copy(self.faceCostas[:])
                colunaParaColuna(aux2, self.faceCostas, colOrigem, (0 if colOrigem == 2 else 2), True)
                colunaParaColuna(aux1, self.faceSuperior, (0 if colOrigem == 2 else 2), colOrigem, True)
            elif ((movimento.face == Faces.esquerda and movimento.sentido == SentidoMovimento.antiHorario) or (movimento.face == Faces.direita and movimento.sentido == SentidoMovimento.horario)):            
                #esquerda anti-horario e direita horario
                colOrigem = (0 if movimento.face == Faces.esquerda else 2)
                aux1 = np.copy(self.faceFrente[:])
                colunaParaColuna(self.faceInferior, self.faceFrente, colOrigem, colOrigem, False)
                aux2 = np.copy(self.faceSuperior[:])
                colunaParaColuna(aux1, self.faceSuperior, colOrigem, colOrigem, False)
                aux1 = np.copy(self.faceCostas[:])
                colunaParaColuna(aux2, self.faceCostas, colOrigem, (0 if colOrigem == 2 else 2), True)
                colunaParaColuna(aux1, self.faceInferior, (0 if colOrigem == 2 else 2), colOrigem, True)
    
def matrizCorVazia():
    #retorna uma matriz de cores vazia
    return [
        [Cores.indefinida, Cores.indefinida, Cores.indefinida],
        [Cores.indefinida, Cores.indefinida, Cores.indefinida],
        [Cores.indefinida, Cores.indefinida, Cores.indefinida]
    ]

#funcao que traduz uma string para um movimento pre-definido nas consts. de Rubik
def stringToMov(mov):
    if (mov == "U"):
        return Rubik.sh
    elif (mov == "U'"):
        return Rubik.sa
    elif (mov == "U2"):
        return Rubik.shDuplo
    elif (mov == "R"):
        return Rubik.dh
    elif (mov == "R'"):
        return Rubik.da
    elif (mov == "R2"):
        return Rubik.dhDuplo
    elif (mov == "F"):
        return Rubik.fh
    elif (mov == "F'"):
        return Rubik.fa
    elif (mov == "F2"):
        return Rubik.fhDuplo
    elif (mov == "D"):
        return Rubik.ih
    elif (mov == "D'"):
        return Rubik.ia
    elif (mov == "D2"):
        return Rubik.ihDuplo
    elif (mov == "L"):
        return Rubik.eh
    elif (mov == "L'"):
        return Rubik.ea
    elif (mov == "L2"):
        return Rubik.ehDuplo
    elif (mov == "B"):
        return Rubik.ch
    elif (mov == "B'"):
        return Rubik.ca
    elif (mov == "B2"):
        return Rubik.chDuplo