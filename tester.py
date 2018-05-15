from rubik.rubik import Rubik
from rubik.algKociemba import resolver
from util.enums import Cores

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

print '\nCubo original:'
cubo.representacaoGrafica()
#grava o tempo antes de iniciar o calculo.
resolver(cubo)
print '\nCubo resolvido:'
cubo.representacaoGrafica()