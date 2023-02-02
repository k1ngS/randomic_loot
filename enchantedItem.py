import random


class EnchantedItem:
    def __init__(self):
        self.encantado_table = {
            4: [
                "O personagem faz jogadas de desafio com 1 dádiva para evitar ficar doente ou se recuperar de uma doença. Ele sofre metade do dano por doença.",
                "O personagem faz jogadas de desafio com 1 dádiva para evitar ficar envenenado ou remover a aflição envenenado. Ele sofre metade do dano por veneno.",
                "O personagem sofre metade do dano por fogo",
                "O personagem não fica fatigado por exposição ao calor ou frio extremo.",
                "O personagem pode utilizar uma ação para fazer o objeto iluminar uma área com raio de 2 metros ao redor dele, até que através de uma ação desencadeada pare o efeito.",
                "Quando o personagem estiver a 100 metros de um demônio, o objeto escurece as sombras ao redor dele, negando sua propriedade horripilante.",
                "O personagem pode falar um idioma adicional, determinado pelo criador do objeto.",
                "O personagem sempre flutua a 2,5 cm do chão,embora ainda sofra dano por aterrissar depois de uma queda.",
                "Quando se move, o personagem pode escolher não emitir nenhum som, independentemente da superfície.",
                "O personagem pode utilizar uma ação para diminuir a luminosidade em um raio de 2 metros ao redor do objeto. Caso esteja iluminada, a área se torna sombras;caso seja sombras, ela se torna escuridão.",
                "Quando tenta escalar, o personagem faz a jogada de desafio de Força com 1 dádiva.",
                "Quando tenta nadar, o personagem faz a jogada de desafio de Força com 1 dádiva.",
                "O personagem aprende uma nova profissão, determinada pelo criador do objeto.",
                "A Percepção do personagem aumenta em 1.",
                "Outros não podem utilizar magia para ler os pensamentos do personagem, nem comunicar-se com ele contra sua vontade.",
                "Caso o objeto seja um recipiente, ele pode conter até quatro vezes seu volume aparente. Caso contrário, quando o objeto é colocado dentro de um recipiente, ele multiplica seu volume por quatro.",
                "O personagem e o objeto nunca ficam sujos.",
                "O personagem sempre sabe a hora exata.",
                "O personagem sempre sabe para onde é o norte.",
                "O objeto tem pernas e age como um construto compelido de seu Tamanho.",
            ],
            8: [
                "O objeto aquece uma área fria com 5 metros de raio ao seu redor, até que a temperatura esteja pouco acima de congelamento.",
                "Quando colocado em um liquido, o objeto afunda e o congela em um raio de 1 metro. Remover a bola congelada do liquido desativa o objeto, e o material descongela naturalmente.",
                "O personagem pode utilizar uma ação para colocar o objeto de uma superficie reta, de 15 cm de espessura, no máximo, ao alcance do personagem. O objeto e a superficie coberta por ele ficam transparentes, até que ele seja removido.",
                "O personagem pode utilizar uma ação para fazer que uma chama rodopiar ao redor do objeto, enquanto ele se concentrar, duração máxima de 1 minuto. As chamas iluminam como uma tocha e causam 1d6 de dano a qualquer coisa que toque, com exceção da criatura que o porta. O objeto tem três cargas, que são recuperadas, uma vez por dia, quando colocado no fogo.",
                "O objeto é venenoso. Qualquer criatura viva que entre em contato com ele sofre 1d6 de dano por veneno, exceto se bem-sucedida em uma jogada de desafio de Força.",
                "O objeto é ameaçador. Criaturas a 5 metros dele fazem suas jogadas de desafio para resistir ficarem assustadas com 1 perdição.",
                "O personagem pode utilizar uma ação para colocar o objeto em qualquer superficie a seu alcance. O objeto fica ali, não importa o que aconteça, até que ele o toque e utilize uma ação para retirá-lo.",
                "O objeto muda de cor e copia perfeitamente o ambiente.",
                "O objeto vibra suavemente, quando a 100 metros de um troll ou gigante.",
                "O personagem pode utilizar uma ação para extinguir todas as chamas a 10 metros de si. O objeto tem três cargas, que são recuperadas, uma vez por dia, quando molhado com água",
                "O objeto fica verde quando está a 10 metros de veneno ou de uma criatura venenosa.",
                "O personagem pode utilizar uma ação para abrir ou fechar todas as portas, recipientes e outros objetos que possam ser abertos e fechados a até 10 metros, como quiser. O objeto tem três cargas.",
                "O objeto emite um campo que afasta insetos normais em uma esfera de 10 metros de raio ao seu redor.",
                "O personagem pode utilizar uma ação desencadeada quando curar dano para curar o dobro da quantidade normal. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para escolher uma criatura alvo ou objeto a até 10 metros e faz uma jogada de desafio de Agilidade contra a Agilidade do alvo. Caso seja bem-sucedido, ele sofre 2d6 de dano de uma das seguintes fontes: ácido, frio, fogo, eletricidade, trovão ou algo à escolha do Mestre. O objeto tem três cargas.",
                "O personagem pode utilizar uma ação para escolher uma criatura viva a até 10 metros dele e fazer uma jogada de ataque de Vontade contra a Vontade do alvo. Caso seja bem-sucedido, ele fica encantado por 1 minuto ou até que sofra dano. O objeto tem três cargas.",
                "O personagem pode utilizar uma ação para voar até 100 metros e pousar com segurança. O objeto tem três cargas.",
                "O personagem utiliza uma ação para lançar o objeto em um espaço aberto no chão a até 20 metros. O objeto desaparece e um animal pequeno compelido surge no local. Ele serve ao personagem por 1 minuto ou até que fique incapacitado. Quando o efeito termina, o animal desaparece e o objeto reaparece no local em que sumiu. O objeto tem uma carga.",
            ],
            12: [
                "O personagem pode utilizar uma ação para fazer o objeto emitir uma música suave, até silenciá-lo através de uma ação desencadeada.",
                "O personagem pode utilizar uma ação desencadeada, a qualquer momento, para fornecer 1 dádiva a qualquer teste que fizer, antes do fim da rodada. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação desencadeada em seu turno para mudar sua aparência, para se parecer com outra pessoa. O efeito dura por 1 hora ou até que sofra dano. Criaturas desconfiadas podem fazer uma jogada de desafio de Percepção para ver através do disfarce. O objeto tem três cargas.",
                "O personagem pode utilizar uma ação para fazer uma névoa se espalhar por 10 metros ao redor do objeto. Ela se mantém por 1 minuto ou até que seja dispersa pelo vento, obscurecendo parcialmente a área. O objeto tem três cargas.",
                "O personagem pode utilizar uma ação para escolher um objeto alvo que possa ver e aprender um fato verdadeiro sobre ele. O objeto tem três cargas.",
                "O personagem pode utilizar uma ação para escolher um ponto no chão a até 20 metros dele. Grama, cipós grossos e outras plantas se espalham pelo chão, a partir daquele ponto, em um raio de 5 metros. O chão da área se torna terreno dificil. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para recuperar a conjuração de uma magia de nivel 1 que conhece. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para transformar o objeto em um outro diferente que não custe mais de 1 xp. A nova forma não possui nenhuma propriedade mágica. Ele mantém a forma até ser usado novamente. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para criar 4 litros de água pura. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para criar um hemisfério opaco permeável com raio de 5 metros centrado no objeto. Ele fica no lugar por 8 horas. O objeto tem uma carga",
                "O personagem pode utilizar uma ação desencadeada em seu turno para se teleportar para um espaço aberto, que possa ver, a até 100 metros. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para escolher um ponto a 100 metros dele. Ele ouve como se estivesse naquele ponto, enquanto se concentrar, por até minuto. O objeto tem três cargas.",
                "O personagem pode utilizar uma ação desencadeada em seu turno para se comunicar telepaticamente com qualquer criatura disposta, que saiba ao menos 1 idioma e esteja a 20 metros dele. O efeito dura por 1 minuto. O objeto tem três cargas.",
                "O personagem move-se sua Distância total em terreno dificil.",
                "O personagem pode utilizar uma ação para fornecer 1 dádiva a todas jogadas de desafio que fizer por 1 minuto. O objeto tem uma carga.",
                "O personagem pode respirar normalmente quando submerso em liquido.",
                "O personagem pode utilizar uma ação para dispersar vapores, gases, névoa, fumaça ou neblina a até 10 metros do objeto. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para reduzir em 1d3 (até um minimo de 0) a quantidade de perdições em jogadas de ataque e jogadas de desafio que fizer por 1 minuto. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para fazer um objeto desaparecer em um espaço extradimensional. A qualquer momento depois disso, ele pode utilizar uma ação para convocar o objeto em sua mão.",
                "O personagem pode utilizar uma ação para fornecer 2 dádivas a sua próxima jogada antes do final da rodada. O objeto tem uma carga."
            ],
            16: [
                "O personagem faz jogadas de desafio com 1 dádiva para identificar ilusões.",
                "O personagem pode utilizar uma ação desencadeada para avançar no tempo. O personagem desaparece e reaparece no fim da rodada, no mesmo espaço ou no espaço aberto mais perto, caso o anterior esteja ocupado. O objeto tem três cargas.",
                "O personagem pode utilizar uma ação desencadeada quando faz uma jogada de ataque de uma magia conjurada por ele para receber 1 dádiva nesta jogada. O objeto tem uma carga.",
                "A cada hora de sono, jogue um d6. Caso o resultado seja 6, o personagem cura 2d6 de dano.",
                "O personagem não pode ser surpreendido.",
                "A distância de pulo do personagem é dobrada.",
                "O personagem pode se mover por, e ficar parado sobre, superficies liquidas, como se fossem chão solido.",
                "O personagem pode utilizar uma ação desencadeada em seu turno para se tornar insubstancial, até o fim da rodada. Enquanto estiver insubstancial, ele sofre metade do dano por armas, pode se mover através de objetos sólidos e outras criaturas, além de ignorar os efeitos de movimentação em terreno dificil. Caso termine o movimento dentro de uma objeto sólido, ele morre instantaneamente. O objeto tem três cargas",
                "Este objeto é uma armadura sem requisito de Força.",
                "Este objeto é uma arma ou muniçaõ que nunca pode se quebrar, nem ser perdida. Quando o personagem é bem-sucedido em uma jogada de ataque com essa arma, ele pode utilizar uma ação desencadeada para aterrorizar o alvo do ataque. Ele fica assustado por 1 rodada, a não ser que seja bem-sucedido em uma jogada de desafio de Vontade.",
                "O objeto brilha toda vez que alguém a 5 metros dele diz uma mentira voluntariamente.",
                "O personagem ganha visão nas sombras.",
                "O personagem aumenta sua taxa de cura em uma quantidade igual a seu nível.",
                "Quando fracassa em uma jogada de desafio exigida por uma magia, o personagem pode utilizar uma ação desencadeada para transformar o fracasso em sucesso. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para transformar o objeto em uma escada de 3 metros. O objeto se mantém nessa forma até que o personagem utilize uma outra ação para transformá-lo novamente.",
                "O personagem pode utilizar uma ação para se transformar em um animal minúsculo. Ele fica nessa forma, no máximo, por 1 hora, até que fique inconsciente ou utilize uma ação desencadeada em seu turno para voltar a sua forma normal. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação para teleportar a si e outras cinco criaturas dispostas a seu alcance instantaneamente e com segurança para um destino escolhido pelo Mestre. O destino pode ser o mesmo a cada uso, ou um diferente. O objeto tem uma carga.",
                "O personagem pode utilizar uma ação desencadeada, quando uma criatura fracassa em uma jogada de ataque com uma arma de combate corpo a corpo para se teleportar até um espaço a 1 metro da criatura desencadeante.",
                "O personagem pode utilizar uma ação para tocar o objeto. O objeto desaparece e se torna uma tatuagem em seu corpo, onde fica até que utilize uma ação desencadeada para recuperá-lo. Uma vez recuperado, o objeto aparece em sua mão ou em um espaço aberto a seu alcance.",
                "O personagem pode utilizar uma ação para se proteger de magia por 1 rodada. Até que o efeito termine, ele faz as jogadas de desafio exigidas por magias ou outros efeitos mágicos com 1 dádiva. Além disso, criaturas fazem jogadas de ataque com 1 perdição, quando o atacam com magias. O objeto tem uma carga."
            ],
            20: [
                "O personagem faz jogadas de desafio de Vontade para evitar ganhar Insanidade com 1 dádiva.",
                "O personagem faz jogadas de desafio para arrombar portas, abrir baús ou levantar objetos pesados com 1 dádiva.",
                "O personagem pode utilizar uma ação para fazer com que um objeto emita um som ensurdecedor em um raio de 10 metros ao redor de si por 1 minuto. Durante este periodo, todas as criaturas na área ficam surdas enquanto ali permanecerem; criaturas a até 100 metros do objeto fazem jogadas de desafio de Percepção para ouvir com 1 perdição. O objeto tem três cargas.",
                "O personagem pode utilizar uma ação desencadeada em seu turno para causar 1d6 de dano adicionar com todos os ataques que fizer durante 1 rodada. O objeto tem três cargas.",
                "O objeto boia e nunca afunda. Ele sempre flutua na superficie de qualquer liquido em que seja colocado.",
                "O objeto é possuido por um demônio minúsculo.Quando o personagem fica incapacitado ele imediatamente cura dano igual a sua taxa de cura e fica controlado pelo demônio por 1 minuto.Consulte Possessão Demoniaca no Capitulo 10.",
                "O objeto é invisivel quando iluminado.",
                "O objeto é uma arma. O personagem reduz em 1 a quantidade de perdições impostas em jogadas para atacar com ele (até o minimo de 0).",
                "Quando o personagem conjura uma magia de nivel 1 ou 2, jogue um d6. Caso o resultado seja 1, ele ganha 1 ponto de Insanidade. Caso o resultado seja 6, ele recupera a conjuração da magia. Qualquer outro resultado não gera efeito.",
                "O personagem não precisa respirar.",
                "O personagem faz jogadas de ataque em ambientes sociais com 1 dádiva.",
                "Quando se move, o personagem não deixa rastros ou os deixa como se fossem de uma criatura a escolha dele.",
                "Áreas de sombras causadas por demônios a até 100 metros se tornam iluminadas, e o personagem fica imune à propriedade horripilante da criatura.",
                "O personagem não precisa comer ou beber.",
                "O personagem não pode ficar assustado.",
                "O objeto toca uma sineta quando se aproxima a 20 metros de uma armadilha.",
                "O objeto contém 1 magia de nível 1 a escolha do Mestre. O personagem pode conjurar a magia do objeto independentemente de seu Poder. A magia tem uma conjuração, que é recuperada uma vez por dia ao amanhecer.",
                "O valor e o modificador de um dos atributos do personagem aumenta em 1, à escolha do Mestre.",
                "O objeto tem duas propriedades. Jogue novamente e ignore os resultados 19 ou 20 nesta tabela",
                "O objeto tem três propriedades. Jogue novamente e ignore os resultados 19 ou 20 nesta tabela",
            ],
        }

    def generate_enchanted_item(self, forma):
        d20 = 18   # random.randint(1, 20)
        twoEffects = []
        threeEffects = []
        limit = 0
        for key in self.encantado_table:
            if d20 <= key:
                efeito = random.choice(self.encantado_table[key])
                if d20 >= 18:
                    if efeito in self.encantado_table[key]:
                        if efeito in self.encantado_table[key][18]:
                            while limit < 2:
                                new = random.choice(self.encantado_table[key])
                                if efeito not in new and new not in twoEffects:
                                    twoEffects.append(new)
                                    limit += 1
                            return f"\nItem encantado ({forma}) com 2 efeitos:     \nEfeito 1°: {twoEffects[0]}\nEfeito 2°: {twoEffects[1]}\n"
                        elif efeito in self.encantado_table[key][19]:
                            while limit < 3:
                                new = random.choice(self.encantado_table[key])
                                if efeito not in new and new not in threeEffects:
                                    threeEffects.append(new)
                                    limit += 1
                            return f"\nItem encantado ({forma}) com 3 efeitos:     \nEfeito 1°: {threeEffects[0]}\nEfeito 2°: {threeEffects[1]}\nEfeito 3°: {threeEffects[2]}\n"
                return f"\nItem encantado ({forma})\nEfeito: {efeito}\n"
        return f"Item encantado ({forma}) sem efeito especial."
