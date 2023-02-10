import random
import tkinter
import customtkinter


class Effect:
    def __init__(self):
        self.dice = lambda x: random.randint(1, x)
        self.injury = {
            4: ['Nocauteado', 'O personagem cai prostrado e fica inconsciente. Ao final de cada rodada, jogue 1d6. Em um resultado par, o personagem remove a aflição inconsciente. O personagem remove a aflição inconsciente. O personagem também remove a aflição quando não estiver mais ferido.'],
            5: ['Ferimento Cambaleante', 'O personagem cai prostrado e fica pasmo por 1 minuto. Ao final de cada rodada, ele pode fazer uma jogada de desafio de Vontade e remover a alição em caso de sucesso. O personagem também remove a aflição quando não estiver mais ferido.'],
            6: ['Ferimento Traumático', 'O personagem ganha 1d3 de Insanidade por ver o seu corpo horrivelmente ferido. Enquanto permanecer assustado por ganhar Insanidade, o personagem também fica debilitado. Resistir a um ferimento traumático deixa uma cicatriz em algum lugar do corpo.'],
            8: ['Ferimento Doloroso', 'Ferimento em um lugar sensível e está abalado pela dor. O personagem fica debilitado por 1 minuto. Ao final de cada rodada, ele pode fazer uma jogada de desafio de Vontade e remover a aflição em caso de sucesso. O personagem também remove a aflição quando não estiver mais ferido.'],
            11: ['Ferimento Menor', 'O personagem sofre um ferimento menor que o deixa debilitado por 1 rodada.'],
            16: ['Hemorragia', 'O personagem sangra profundamente a partir do ferimento. Ao final de cada rodada, ele recebe 1d6 de dano pelo ferimento. Múltiplas hemorragias possuem um efeito cumulativo. Quando recebe este dano, o personagem fica fatigado por 1 rodada. Uma criatura ao alcance do personagem pode estancar o ferimento e remover a condição de hemorragia com um sucesso em um jogada de desafio de Intelecto. Usar um kit de curandeiro concede 1 dádiva para a jogada.\n Caso o personagem não seja uma criatura viva, ao invés de Hemorragia, ele recebe -1d6 de penalidade na Saúde a cada vez que sofre este efeito. Esta penalidade dura até o personagem completar um descanso.'],
            19: ['Aleijado', 'O personagem perde uma extremidade e fica pasmo por 1 rodada. Jogue na tabela a seguir para determinar o membro ou os membros perdido(s).'],
            21: ['Perda de um Membro', 'O personagem perde um membro. Este pode ter sido amputado, esmagado ou mutilado ao ponto de se tornar inútil. O personagem fica atordoado por 1 minuto e sofre também uma Hemorragia. Jogue 2d6 para determinar qual membro é perdido. Para determinar se é o direito ou o esquerdo, jogue 1d6, com um resultado par indicando o membro direito e um resultado ímpar o membro esquerdo. Os efeitos da perda de um membro são óbvios.\n - O personagem sem uma perna, ou sem a parte de uma perna, não pode andar sem ajuda. Também, perder o pé ou a perna faz com que o personagem caia prostrado e impede que ele permaneça de pé.'],
            22: ['Coma', 'O personagem perde os sentidos e cai em um coma que dura 1d3 semanas. A menos que seja alimentado e hidratado, ele eventualmente morre.'],
            23: ['Ferimento Horrível', 'Sangue jorra do corpo do personagem, o choque causa a falência dos órgãos ou algo fundamental para o seu bem estar deixa de funcionar. O personagem cai prostrado e fica debilitado. Além de tudo isso, o personagem morre em 1d3 rodadas. A morte pode ser prevenida caso o personagem cure algum dano e o dano total após a cura indique que o personagem não está mais ferido. Caso sobreviva, O personagem ganha uma cicatriz desagradável para se lembrar do que o entrava. Jogue 1d6 para ver o que acontece.'],
            24: ['Ferimento Catastrófico', 'O personagem morre e o seu corpo, ou o que sobrou dele, cai prostrado.']
        }
        self.scar_table = {
            1: 'Cabeça',
            2: 'Testa',
            3: 'Bochecha',
            4: 'Orelha',
            5: 'Queixo',
            6: 'Nariz',
            7: 'Mão',
            8: 'Antebraço',
            9: 'Parte Superior do Braço',
            10: 'Peito',
            11: 'Abdômen',
            12: 'Ombro',
            13: 'Costelas',
            14: 'Parte Superior das Costas',
            15: 'Parte Inferior das Costas',
            16: 'Nádegas',
            17: 'Pé',
            18: 'Panturrilha',
            19: 'Cintura',
            20: 'Virilha'
        }
        self.table = {
            1: 'Perde um pedaço da pele.',
            2: 'Perde 1 orelha. Caso o personagem perca as duas orelhas, ele faz suas jogadas de desafio de Percepção com 3 perdições.',
            3: f'Perde {self.dice(3)} dedos do pé.', 4: f'Perde {self.dice(3)} dedos da mão', 5: f'Perde o nariz, Caso não tenha nariz, trate este resultado como se fosse 1( Perde um pedado da pele. )', 6: 'Perde 1 olho, Caso o personagem perca ambós os olhos, ele fica cego.'
        }
        self.limb_table = {
            2: 'Braço Inteiro. Caso perca ambos os braços, o personagem morre.',
            5: 'Antebraço. Caso o personagem não tenha o antebraço. Ele perde o braço inteiro.',
            7: 'Mão. Caso o personagem não tenha a mão. Ele perde o antebraço.',
            9: 'Pé. Caso o personagem não tenha o pé. Ele perde a parte inferior da perna.',
            11: 'Parte Inferior da Perna. Caso o personagem não tenha a parte inferior da perna. Ele perde a perna inteira.',
            12: 'Perna Inteira. Caso perca ambas as pernas, o personagem morre.'
        }

    def get_scar(self):
        d20 = self.dice(20)
        return self.scar_table[d20]
