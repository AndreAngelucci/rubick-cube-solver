from vision.analiseCores import gerarRubikImagem
from util.funcoesUteis import printLogo
from rubik.rubik import *
from rubik.algKociemba import resolver

#gera uma cubo randomico
printLogo()
cubo = rubikMontado()
print '\nCubo montado:'
cubo.representacaoGrafica()
print '\nExecucao de 50 movimentos aleatorios:'
cubo.movimentosRandom(50)
print 'Cubo baguncado:'
cubo.representacaoGrafica()
resolver(cubo)
print '\nCubo resolvido:'
cubo.representacaoGrafica()
