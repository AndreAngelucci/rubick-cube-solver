from rubik import *
from enums import *
from algKociemba import resolver
from operacoesMatriz import *

cubo = Rubik(
    [
        [Cores.verde, Cores.azul   , Cores.azul    ],
        [Cores.azul , Cores.branco , Cores.branco  ],
        [Cores.azul , Cores.laranja, Cores.vermelho]
    ],
    [
        [Cores.branco  , Cores.laranja, Cores.azul   ],
        [Cores.vermelho, Cores.laranja, Cores.verde  ],
        [Cores.branco  , Cores.laranja, Cores.laranja]
    ],
    [
        [Cores.amarelo , Cores.branco, Cores.branco ],
        [Cores.vermelho, Cores.azul  , Cores.amarelo],
        [Cores.amarelo , Cores.azul  , Cores.laranja]
    ],
    [
        [Cores.vermelho, Cores.azul   , Cores.laranja ],
        [Cores.vermelho, Cores.verde  , Cores.amarelo ],
        [Cores.laranja , Cores.amarelo, Cores.vermelho]
    ],
    [
        [Cores.amarelo , Cores.verde   , Cores.verde  ],
        [Cores.vermelho, Cores.vermelho, Cores.branco ],
        [Cores.azul    , Cores.verde   , Cores.amarelo]
    ],
    [
        [Cores.vermelho, Cores.branco , Cores.verde ],
        [Cores.laranja , Cores.amarelo, Cores.verde ],
        [Cores.verde   , Cores.amarelo, Cores.branco]
    ]
)

m = [
    [0, 1, 2],
    [3, 5, 2],
    [3, 2, 2]
]
m2 = [
    [4, 4, 4],
    [3, 5, 2],
    [3, 2, 2]
]

print '\nCubo original:'
cubo.representacaoGrafica()
resolver(cubo)
print '\nCubo resolvido:'
cubo.representacaoGrafica()

#TEM ALGUMA COISA ERRADA NA MOVIMENTAcaO DOS VIZINHOS SUPERIORES