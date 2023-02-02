class LootTable:
    def __init__(self):
        self.loot_table = {
            1: "nada",
            2: "2 centavos de cobre",
            3: "1 XP",
            4: "Poção de cura",
            5: {
                'name': 'Feitiço',
                'feiticos': {
                    1: 'Feitiço: Teurgia',
                    2: 'Feitiço: Batalha',
                    3: 'Feitiço: Celestial',
                    4: 'Feitiço: Primitiva',
                    5: 'Feitiço: Arcana',
                    6: 'Feitiço: Natureza'
                }
            },
            6: {
                'name': 'Item encantado',
                'forma': {
                    1: "Armadura Leve",
                    2: "Arma de Combate Corpo a Corpo",
                    3: "Joias",
                    4: "Móveis",
                    5: "Escultura",
                    6: "Moeda",
                    7: "Ferramenta",
                    8: "Roupas",
                    9: "Instrumento",
                    10: "Recipiente",
                    11: "Inscrição",
                    12: "Implemento",
                    13: "Tecnologia",
                    14: "Jogo ou brinquedo",
                    15: "Acessório",
                    16: "Veículo",
                    17: "Religioso",
                    18: "Estranho",
                    19: "Arma de Combate à Distância",
                    20: "Armadura Média/Pesada",
                }
            }
        }
