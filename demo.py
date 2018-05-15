from vision.analiseCores import gerarRubikImagem
from util.funcoesUteis import printLogo
from rubik.rubik import *
from rubik.algKociemba import resolver

#gera uma cubo randomico
printLogo()
print 'Demonstracao da abstracao e resolucao do Cubo de Rubik:'
cubo = rubikMontado()
print '\nPosicionamento inicial do cubo:'
cubo.representacaoGrafica()
print '\nCubo apos a execucao de 50 movimentos randomicos:'
cubo.movimentosRandom(50)
print '\nExecucao do algoritimo de solucao:'
cubo.representacaoGrafica()
resolver(cubo)
print '\nCubo resolvido:'
cubo.representacaoGrafica()
