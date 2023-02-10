class Spell:
    def __init__(self):
        self.spellList = {
            'tipos': {
                'teurgia': {
                    0: {
                        'nome': 'Censura Teurgia AT.1',
                        'tipo': 'Área: Uma esfera com 5 metros de raio, centra em um ponto ao alcance do conjurador.',
                        'duracao': '1 minuto',
                        'efeito': 'O conjurador apresenta seu símbolo sagrado, um pedaço de escritura ou algum tipo de representação física de sua fé e libera uma onde de poder sagrado que se dispersa pela área. Cada demônio, espírito, fada, diabo e morto-vivo na área deve fazer uma jogada de desafio de Vontade. Caso fracasse, a criatura fica assustada por 1 minuto.',
                        '+20': None
                    },
                    1: {
                        'nome': 'Criar Símbolo Sagrado Teurgia UT.0',
                        'tipo': None,
                        'duracao': '1 minuto',
                        'efeito': 'Um símbolo sagrado brilhante surge na mão do conjurador e se mantém pela duração da magia ou até ser derrubado. O símbolo sagrado fornece uma dádiva para as jogadas de ataque com magias de Teurgia do conjurador.',
                        '+20': None
                    },
                    2: {
                        'nome': 'Acusar Teurgia AT.0',
                        'tipo': 'Alvo: Uma criatura a curta distância que possa ver e ouvir o conjurador.',
                        'duracao': None,
                        'efeito': 'O conjurador apresenta seu símbolo sagrado e faz uma jogada de ataque de Vontade contra a Vontade do alvo. Caso seja bem-sucedido, ele fica assustado por 1 rodada.',
                        '+20': 'O alvo também fica prostrado.'
                    },
                    3: {
                        'nome': 'Benção Teurgia UT.1',
                        'tipo': 'Alvo: Qualquer quantidade de criaturas ao alcance do conjurador.',
                        'duracao': '1 minuto',
                        'efeito': 'O conjurador toca cada um e concede sua benção. Enquanto durar a magia, o alvo faz jogadas de ataque e de desafio com 1 dádiva e não pode ser assustado.',
                        '+20': None
                    },
                    4: {
                        'nome': 'Martelo de Deus Teurgia AT.2',
                        'tipo': 'Alvo: Um ponto no espaço a média distância.',
                        'duracao': '1 minuto',
                        'efeito': 'Um martelo brilhante dourado surge no alvo e flutua. Enquanto durar a magia, o conjurador pode utilizar uma ação desencadeada em seu turno para mover o martelo até 10 metros e atacar uma criatura a 1 metro dele. O conjurador faz uma jogada de ataque de Vontade com 1 dádiva contra a Defesa do alvo. Caso seja bem-sucedido, o alvo sofre 2d6 de dano.',
                        '+20': 'O alvo sofre 2d6 de dano adicional.'
                    },
                    5: {
                        'nome': 'Auxílio Divino Teurgia UT.3',
                        'tipo': 'Alvo: Criaturas escolhidas pelo conjurador a curta distância;',
                        'duracao': '1 hora',
                        'efeito': 'Cada alvo recebe um bônus de +15 para Saúde enquanto durar a magia.',
                        '+20': None
                    },
                },
                'batalha': {
                    0: {
                        'nome': 'Ataque Ampliado Batalha AT.0',
                        'tipo': None,
                        'duracao': None,
                        'efeito': 'Como parte da conjuração desta magia, o conjurador faz um ataque com uma arma. O conjurador faz a jogada de ataque com 1 dádiva e pode utilizar Intelecto ao invés do atributo normal do ataque.',
                        '+20': None
                    },
                    1: {
                        'nome': 'Celeridade Batalha UT.0',
                        'tipo': None,
                        'duracao': None,
                        'efeito': 'O conjurador se move até o dobro do Deslocamento.\nEste movimento não desencadeia ataques livres.\n\nDesencadeado: O conjurador pode utilizar uma ação desencadeada em seu turno para conjurar esta magia. Caso faça isso, ele se move até seu Deslocamento normal sem desencadear ataques livres.',
                        '+20': None
                    },
                    2: {
                        'nome': 'Ataque Poderoso Batalha AT.1',
                        'tipo': None,
                        'duracao': None,
                        'efeito': 'Como parte da conjuração desta magia, o conjurador faz um ataque com uma arma. Ele faz a jogada de ataque com 1 dádiva e pode utilizar Intelecto ao invés do atributo normal do ataque. Caso seja bem-sucedido, o alvo sofre 2d6 de dano adicional.',
                        '+20': None
                    },
                    3: {
                        'nome': 'Fechar Ferimentos Batalha UT.1',
                        'tipo': None,
                        'duracao': None,
                        'efeito': 'O conjurador cura uma quantidade de pontos de dano igual sua taxa de cura.\n\nDesencadeado: O conjurador pode utilizar uma ação desencadeada em seu turno para conjurar essa magia. Caso faça isso, ele cura uma quantidade de pontos de dano igual à metade de sua taxa de cura.',
                        '+20': None
                    },
                    4: {
                        'nome': 'Arco da Morte Batalha AT.2',
                        'tipo': 'Alvo Cada criatura escolhida ao alcance do conjurador',
                        'duracao': '1 minuto',
                        'efeito': 'O conjurador desliza sua arma de combate corpo a corpo ao redor de si em um arco mortal, causando 3d6+3 de dano a cada alvo ao invés do dano normal da arma. Cada alvo sofre metade do dano se bem-sucedido em uma jogada de desafio de Agilidade.',
                        '+20': None
                    },
                    5: {
                        'nome': 'Aptidão para a Batalha UT.3',
                        'tipo': None,
                        'duracao': '1 minuto',
                        'efeito': 'O conjurador amplia suas habilidades de batalha.\nEnquanto durar a magia, toda vez que atacar com uma arma, ele pode fazer a jogada de ataque duas vezes e utilizar o melhor resultado. Além disso, seus ataques com arma causam 1d6 de dano adicional até o fim do efeito.',
                        '+20': None
                    },

                },
                'celestial': {
                    0: {
                        'nome': 'Feixe Ardente Celestial AT.0',
                        'tipo': 'Alvo: Uma criatura ou objeto a média distância.',
                        'duracao': None,
                        'efeito': 'Um feixe flamejante escapa da mão do conjurador. Ele faz uma jogada de ataque de Vontade contra a Agilidade do alvo. Caso seja bem-sucedido, o alvo sofre 1d6 de dano adicional.',
                        '+20': 'O alvo fica cego por 1 rodada.'
                    },
                    1: {
                        'nome': 'Clarão Celestial AT.1',
                        'tipo': 'Alvo: Uma criatura dentro do campo de visão a curta distância',
                        'duracao': None,
                        'efeito': 'Um clarão de luz brilhante surge na frente do alvo. O conjurador faz uma jogada de ataque de Vontade contra a Percepção do alvo. Caso seja bem-sucedido, o alvo fica cego por 1 rodada.',
                        '+20': None
                    },
                    2: {
                        'nome': 'Luz Persistente Celestial UT.1',
                        'tipo': 'Alvo: Um objeto ao alcance do conjurador',
                        'duracao': '8 horas',
                        'efeito': 'O conjurador toca o objeto e uma luz brilha a partir dele em um raio de 10 metros pelo tempo de duração da magia..',
                        '+20': None
                    },
                    3: {
                        'nome': 'Explosão Prismática Celestial AT.1',
                        'tipo': 'Alvo: Um ponto no espaço a média distância',
                        'duracao': None,
                        'efeito': 'Uma partícula brilhante voa do dedo do conjurador em direção ao alvo. Quando alcança o ponto alvo, ou caso encontre uma criatura ou objeto sólido antes dele, a partícula explode em luzes coloridas. Elas se dispersam em ponto na criatura ou objeto. Cada criatura capaz de enxergar na área deve ser bem-sucedida em uma jogada de desafio de Percepção ou fica pasma por 1 rodada.',
                        '+20': None
                    },
                    4: {
                        'nome': 'Raios Solares Celestial AT.2',
                        'tipo': 'Alvo: Até três criaturas ou objetos a média distância',
                        'duracao': None,
                        'efeito': 'Três raios, flamejantes voam para fora da mão do conjurador, divididos como ele escolher entre seus alvos. Para cada raio, ele faz uma jogada de ataque de Vontade contra a Agilidade do alvo. Caso seja bem-sucedido, o alvo também fica debilitado por 1 rodada.',
                        '+20': 'O alvo sofre 1d3 de dano adicional.'
                    },
                    5: {
                        'nome': 'Estrela Cadente Celestial AT.3',
                        'tipo': 'Alvo: Um ponto no espaço a média distância',
                        'duracao': None,
                        'efeito': 'Uma partícula de luz branca aparece em qualquer lugar dentro do alcance da magia e corre em direção ao alvo.\nQuando alcança este ponto, ou caso encontre uma criatura ou objeto sólido antes, a partícula explode. Chamas se dispersam por uma esfera de 3 metros de raio centrada no alvo ou em um ponto no espaço da criatura ou objeto, causando 2d6+2 de dano a tudo na área. Casa criatura na área deve fazer uma jogada de desafio de Força.\nA criatura fica debilitada por 1 rodada em caso de falha, ou apenas sofre metade do dano em caso de sucesso.',
                        '+20': None
                    },

                },
                'primitiva': {
                    0: {
                        'nome': 'Fera Interior Primitiva UT.0',
                        'tipo': None,
                        'duracao': '1 minuto',
                        'efeito': 'Os olhos do conjurador brilham, pelos cobrem seu corpo, as unhas crescem formando garras e os dentes se tornam presas. Enquanto durar a magia, ele ganha visão no escuro e um bônus de +2 no Deslocamento, seus ataques desarmados e armas naturais causam 1d6 de dano adicional.',
                        '+20': None
                    },
                    1: {
                        'nome': 'Amizade Animal Primitiva AT.1',
                        'tipo': 'Alvo: Um animal que possa ver o conjurador a curta distância.',
                        'duracao': None,
                        'efeito': 'O conjurador faz uma jogada de ataque de Vontade contra a Vontade do alvo. Ele faz uma jogada de ataque com 1 dádiva, se estiver sob o efeito da magia idioma das feras. Caso a Saúde do alvo seja maior que a do conjurador, a magia fracassa e a conjuração é perdida.Caso seja bem-sucedido, o alvo fica encantado até que o conjurador complete um descanso. Ele o acompanha em suas aventuras e o ajuda da melhor maneira possível, embora permaneça sob controle do Mestre.O conjurador pode ter uma quantidade igual ao seu Poder de animais encantados desta forma. Caso a conjuração desta magia exceda essa quantidade, o efeito termina automaticamente no animal afetado há mais tempo.',
                        '+20': 'O alvo fica permanentemente encantado.'
                    },
                    2: {
                        'nome': 'Convocar Animal Pequeno Primitiva UT.1',
                        'tipo': 'Área: Um cubo de espaço, com 1 metro de lado, originado em ponto a média distância sob uma superfície sólida.',
                        'duracao': '1 hora',
                        'efeito': 'Um animal pequeno ou minúsculo compelido aparece na área. O animal minúsculo pode ter uma das seguintes propriedades: escalador, nadador, venenoso ou voador.O animal é de um tipo apropriado ao ambiente no qual o personagem conjurou esta magia. Quando o efeito termina, o animal fica incapacitado, voltando para onde veio.',
                        '+20': None
                    },
                    3: {
                        'nome': 'Fera Atroz Primitiva UT.2',
                        'tipo': 'Alvo: O conjurador ou um animal a curta distância.',
                        'duracao': '1 minuto',
                        'efeito': 'O alvo se torna uma besta selvagem. Enquanto durar a magia, o Tamanho do alvo aumenta para 1 ou aumenta em 1, caso seja de Tamanho 1 ou maior, seus ataques com golpes desarmados ou armas naturais causam 1d6 de dano adicional.',
                        '+20': None
                    },
                    4: {
                        'nome': 'Bote Primitiva AT.3',
                        'tipo': 'Requisitos: O conjurador deve estar sob efeito da magia fera interior.',
                        'duracao': None,
                        'efeito': 'O conjurador se desloca até o dobro de seu Deslocamento. A qualquer momento durante esse movimento, ele pode fazer um ataque desarmado ou com uma arma natural contra um alvo a seu alcance, utilizando Vontade no lugar do atributo que o ataque utilizaria normalmente. Caso seja bem-sucedido, o alvo sofre o dano do ataque mais 2d6 de dano adicional e fica prostrado.',
                        '+20': None
                    },
                    5: {
                        'nome': 'Convocar Animal Grande Primitiva UT.3',
                        'tipo': 'Área: Um cubo de espaço, com 2 metros de lado, originado em ponto a média distância sob uma superfície sólida.',
                        'duracao': '1 hora',
                        'efeito': 'Esta magia funciona como convocar animal pequeno, exceto que um animal grande, médio ou pequeno aparece na área. Um animal médio ou pequeno pode ter uma dos seguintes propriedades: escalador, nadador, venenoso ou voador.',
                        '+20': None
                    },

                },
                'arcana': {
                    0: {
                        'nome': 'Dardo Mágico Arcana AT.0',
                        'tipo': 'Alvo: Uma criatura ou objeto a longa distância.',
                        'duracao': None,
                        'efeito': 'Um dardo mágico voa da ponta do dedo do conjurador. O dardo acerta automaticamente, se o caminho entre o conjurador e o alvo não estiver obstruído. O alvo sofre 1d3+1 de dano.',
                        '+20': None
                    },
                    1: {
                        'nome': 'Armadura Arcana UT.0',
                        'tipo': 'Requisitos: O conjurador não deve estar vestindo armadura.',
                        'duracao': '4 horas',
                        'efeito': 'Um campo de força invisível surge ao redor do conjurador, fornecendo um bônus de +2 para sua Defesa, enquanto durar a magia. Além disso, enquanto a magia está em efeito, precipitação normal não toca o conjurador, ventos suaves não o afetam e ele não sente desconforto por frio ou calor, embora ainda sofra dano por fogo e frio.',
                        '+20': None
                    },
                    2: {
                        'nome': 'Visão Arcana Arcana UT.1',
                        'tipo': None,
                        'duracao': '1 minuto',
                        'efeito': 'Pela duração da magia, o conjurador vê auras ao redor de criaturas, objetos e áreas afetadas por magia. A critério do Mestre, ele talvez possa aprender a qual tradição a magia pertence.',
                        '+20': None
                    },
                    3: {
                        'nome': 'Dardos Infalíveis Arcana AT.1',
                        'tipo': 'Alvo: Uma a três criaturas ou objetos a longa distância.',
                        'duracao': None,
                        'efeito': 'Sete dardos mágicos voam para fora das pontas dos dedos do conjurador, divididos como ele escolher entre seus alvos. Cada dardo acerta automaticamente, se o caminho entre o conjurador e os alvos não estiver obstruído. O alvo sofre 1 de dano para cada dardo que o atingir.',
                        '+20': None
                    },
                    4: {
                        'nome': 'Dardos Explosivos Arcana AT.2',
                        'tipo': 'Alvo: Uma a três criaturas ou objetos a longa distância.',
                        'duracao': None,
                        'efeito': 'Três dardos mágicos voam para fora das pontas dos dedos do conjurador, divididos como ele escolher entre seus alvos. Cada dardo acerta automaticamente, se o caminho entre o conjurador e os alvos não estiver obstruído. Cada dardo causa 1 de dano em seu alvo e em seguida explode em um raio de 1 metro de um ponto dentro do espaço do alvo. Tudo na área sofre 1d6+1 de dano, ou metade do dano, caso o alvo seja bem-sucedido em uma jogada de desafio de Agilidade.',
                        '+20': None
                    },
                    5: {
                        'nome': 'Destruir Magia Arcana UT.3',
                        'tipo': 'Alvo: Um cubo, com 5 metros de lado, originado de um ponto a média distância.',
                        'duracao': None,
                        'efeito': 'Todos os efeitos criados por magias de nível 3 ou menos que estejam ativos em qualquer coisa na área terminam imediatamente.',
                        '+20': None
                    },

                },
                'natureza': {
                    0: {
                        'nome': 'Bolotas Mágicas Natureza AT.0',
                        'tipo': 'Alvo: Até cinco bolotas, nozes ou sementes ao alcance do conjurador.',
                        'duracao': '1 hora',
                        'efeito': 'O conjurador toca os alvos, imbuindo cada um com magia que dura até o fim do efeito ou até serem usados por uma criatura. Ela pode atacar com as bolotas ao arremessá-las contra criaturas ou objetos a curta distância, fazendo uma jogada de ataque de Agilidade contra a Agilidade do alvo. Caso obtenha sucesso, ele sofre 1d3 de dano e fica lento por 1 rodada. Caso seja incapacitado por esse dano, o alvo se enraíza no chão e se transforma em um broto permanentemente.',
                        '+20': 'O alvo sofre 1d6 de dano adicional'
                    },
                    1: {
                        'nome': 'Pele de Carvalho Natureza UT.0',
                        'tipo': None,
                        'duracao': '1 hora',
                        'efeito': 'Enquanto durar a magia, o conjurador ganha um bônus de +2 para sua Defesa. Além disso, quando tenta se esconder em ambientes de floresta, ele faz jogadas de desafio de Agilidade com 1 dádiva.',
                        '+20': None
                    },
                    2: {
                        'nome': 'Shillelagh Natureza UT.1',
                        'tipo': 'Alvo: Um porrete ou cajado empunhado pelo conjurador',
                        'duracao': '1 hora',
                        'efeito': 'O conjurador imbui a arma alvo com magia que dura até o fim do efeito ou até que ele o solte. Enquanto segura a arma alvo, o conjurador recebe um bônus de +2 para seu Deslocamento e ataques, também causa 1d6 de dano adicional.',
                        '+20': None
                    },
                    3: {
                        'nome': 'Exuberância Natureza UT.1',
                        'tipo': 'Área: Um círculo no solo com 10 metros de raio, centrado em um ponto a média distância.',
                        'duracao': '1 hora',
                        'efeito': 'Ervas e cipós se espalham por uma área, que se torna terreno difícil enquanto durar a magia. Quando o efeito termina, o crescimento resseca e morre.',
                        '+20': None
                    },
                    4: {
                        'nome': 'Vinhas Enredantes Natureza AT.2',
                        'tipo': 'Alvo: Até cinco criaturas a média distância.',
                        'duracao': None,
                        'efeito': 'Vinhas irrompem sob os alvos. Cada alvo deve obter sucesso em um teste de Agilidade ou fica imobilizado por 1 minuto. O alvo pode utilizar uma ação para remover a aflição, arrancando as vinhas.',
                        '+20': None
                    },
                    5: {
                        'nome': 'Espinheiro Natureza UT.3',
                        'tipo': 'Área: Um círculo no solo com 10 metros de raio',
                        'duracao': '1 minuto',
                        'efeito': 'Espinheiros com espinhos afiados como navalhas se espalham pela área, que se torna terreno difícil enquanto durar a magia. Quando o efeito termina, o espinheiro resseca e morre. Qualquer criatura que entre na área ou se mova através dela deve fazer uma jogada de desafio de Agilidade com 1 perdição, sofrendo 1d6 de dano, caso fracasse.',
                        '+20': None
                    },

                }
            },
        }
