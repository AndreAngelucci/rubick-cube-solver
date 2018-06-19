from vision.analiseCores import gerarRubikImagem
from util.funcoesUteis import printLogo
from rubik.rubik import *
from rubik.algKociemba import resolver

#gera uma cubo randomico
printLogo()
print 'Abstracao e resolucao do Cubo de Rubik.'
raw_input("\nPressione Enter para continuar...")
cubo = rubikMontado()
print '\nPosicionamento inicial do cubo:'
cubo.representacaoGrafica()
print 'Serao efetuados movimentos aleatorios para simular um cubo embaralhado.'
movs = input('Quantidade de movimentos: ')
print '\nCubo apos a execucao de {} movimentos randomicos:'.format(movs)
cubo.movimentosRandom(movs)
cubo.representacaoGrafica()
raw_input("\nPressione Enter para executar o algoritmo de solucao...")
print '\nExecucao do algoritimo de solucao:'
resolver(cubo)
raw_input("\nPressione Enter para continuar...")
print '\nCubo resolvido:'
cubo.representacaoGrafica()
