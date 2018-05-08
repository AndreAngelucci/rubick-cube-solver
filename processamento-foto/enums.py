from enum import Enum

#enum com as cores do cubo
class Cores(Enum):
	branco = 0
	laranja = 1
	azul = 2
	verde = 3
	amarelo = 4
	vermelho = 5
	indefinida = 6

#possiveis faces do cubo
class Faces(Enum):
    frente = 0
    superior = 1
    direita = 2
    esquerda = 3
    inferior = 4
    costas = 5

#possiveis movimentos
class SentidoMovimento(Enum):
    horario = 0
    antiHorario = 1	

#tipos de peca
class Pecas(Enum):
    central = 0
    meio = 1
    lateral = 2