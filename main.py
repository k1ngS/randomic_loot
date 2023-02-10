import tkinter
import customtkinter
import random

from tkinter import scrolledtext

from lootTable import LootTable
from enchantedItem import EnchantedItem
from spells import Spell
from monstersTable import Monster
from effects import Effect

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')


class App(customtkinter.CTk):

    frames = {'main_frame': None, 'spell_frame': None,
              'monster_frame': None, 'effect_frame': None}

    def main_frame_selector(self):
        App.frames['spell_frame'].pack_forget()
        App.frames['monster_frame'].pack_forget()
        App.frames['effect_frame'].pack_forget()
        App.frames['main_frame'].pack(
            in_=self.right_side_container, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=(100, 0))
        self.bt_from_main_frame.place(
            in_=self.right_side_container, relx=0.85, rely=0.22, anchor='center')
        self.effects.dices.place(in_=self.right_side_container,
                                 relx=0.85, rely=0.08, anchor='center')
        self.show_num_chests_checkbox.place(
            in_=self.right_side_container, relx=0.12, rely=0.22, anchor='center')

    def spell_frame_selector(self):
        App.frames['main_frame'].pack_forget()
        App.frames['monster_frame'].pack_forget()
        App.frames['effect_frame'].pack_forget()
        App.frames['spell_frame'].pack(
            in_=self.right_side_container, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        self.bt_from_main_frame.place_forget()
        self.effects.dices.place_forget()
        self.show_num_chests_checkbox.place_forget()

    def monster_frame_selector(self):
        App.frames['main_frame'].pack_forget()
        App.frames['spell_frame'].pack_forget()
        App.frames['effect_frame'].pack_forget()
        App.frames['monster_frame'].pack(
            in_=self.right_side_container, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def effect_frame_selector(self):
        App.frames['main_frame'].pack_forget()
        App.frames['spell_frame'].pack_forget()
        App.frames['monster_frame'].pack_forget()
        App.frames['effect_frame'].pack(
            in_=self.right_side_container, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def __init__(self):
        super().__init__()
        self.loot_table = LootTable()
        self.enchanted_item = EnchantedItem()
        self.spells = Spell()
        self.monsters = Monster()
        self.effects = Effect()

        # Configuração do programa
        self.title('RPGLootHelper')
        self.geometry('800x400')
        self.resizable(False, False)
        self.wm_iconbitmap('favicon.ico')

        main_container = customtkinter.CTkFrame(self)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # Sidebar + buttões
        left_side_panel = customtkinter.CTkFrame(main_container, width=150)
        left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y,
                             expand=False, padx=10, pady=10)

        # Botão Gerador de Loot
        bt_main_frame = customtkinter.CTkButton(
            left_side_panel, text='Loot', command=self.main_frame_selector)
        bt_main_frame.grid(row=0, column=0, padx=20, pady=10)

        # Botão Lista de Feitiços
        bt_spell_frame = customtkinter.CTkButton(
            left_side_panel, text='Spell List', command=self.spell_frame_selector)
        bt_spell_frame.grid(row=1, column=0, padx=20, pady=10)

        # Botão Gerador de Monstros
        bt_monster_frame = customtkinter.CTkButton(
            left_side_panel, text='Monster', command=self.monster_frame_selector)
        bt_monster_frame.grid(row=2, column=0, padx=20, pady=10)

        # Botão Gerador de Ferimento
        bt_effect_frame = customtkinter.CTkButton(
            left_side_panel, text='Ferimento', command=self.effect_frame_selector)
        bt_effect_frame.grid(row=3, column=0, padx=20, pady=10)

        # Footer Creditos
        myCredits = customtkinter.CTkLabel(
            left_side_panel, text='created by k1ngS')
        myCredits.grid(row=10, column=0, pady=140)

        # Criando painel direito para ficar alojado os Frames Principais
        self.right_side_panel = customtkinter.CTkFrame(main_container)
        self.right_side_panel.pack(
            side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.right_side_container = customtkinter.CTkFrame(
            self.right_side_panel, fg_color="#000811")
        self.right_side_container.pack(
            side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # Frame de Loot
        App.frames['main_frame'] = customtkinter.CTkFrame(
            main_container)
        self.bt_from_main_frame = customtkinter.CTkButton(
            main_container, text='Gerar Loot', command=self.roll_dice)
        self.bt_from_main_frame.place_forget()

        # Combox dos dados de d6 até d20
        self.effects.dices = customtkinter.CTkOptionMenu(
            main_container, values=['D6', 'D8', 'D10', 'D12', 'D20'])
        self.effects.dices.place_forget()

        # Checkbox dos baus
        self.show_num_chests = tkinter.StringVar()
        self.show_num_chests_checkbox = customtkinter.CTkCheckBox(
            master=main_container, text='+bau?', command=self.toggle_spinbox, variable=self.show_num_chests, onvalue='on', offvalue='off')
        self.show_num_chests_checkbox.place_forget()

        # Spinbox dos baus
        self.num_chests = tkinter.IntVar()
        self.num_chests.set(1)
        self.num_chests_spinbox = tkinter.Spinbox(
            self.right_side_container, from_=1, to=100, width=5, textvariable=self.num_chests)

        # Resultado dos Loots
        self.result_text = scrolledtext.ScrolledText(
            App.frames['main_frame'])
        self.result_text.configure(
            state='disabled', background='#000811', fg='white')
        self.result_text.pack()

        # Frame da Lista de Spells
        App.frames['spell_frame'] = customtkinter.CTkFrame(
            main_container, fg_color='blue')
        self.spell_list = scrolledtext.ScrolledText(
            App.frames['spell_frame'])
        self.spell_list.pack()

        self.spell_list.delete('1.0', tkinter.END)
        self.spell_list_func()
        self.spell_list.configure(
            state='disabled', background='#000811', fg='white')

        # Frame do Gerador de Monstros
        self.table_entries = []
        App.frames['monster_frame'] = customtkinter.CTkFrame(
            main_container, fg_color='#000811')

        self.frame_generator_monster = customtkinter.CTkFrame(
            App.frames['monster_frame'], fg_color="#000811")
        self.frame_generator_monster.grid(row=1, column=0, columnspan=2)

        self.bMonster = customtkinter.CTkButton(
            App.frames['monster_frame'], text='Gerar monstro', command=self.generate_monster)
        self.bMonster.grid(row=0, column=1, columnspan=2, pady=(40, 40))
        App.frames['monster_frame'].columnconfigure(0, weight=1)
        App.frames['monster_frame'].columnconfigure(1, weight=1)
        App.frames['monster_frame'].columnconfigure(2, weight=1)

        self.checkbox_multiple_monsters_var = tkinter.BooleanVar()

        self.checkbox_multiple_monsters = tkinter.Checkbutton(App.frames['monster_frame'],
                                                              text="Múltiplos monstros",
                                                              variable=self.checkbox_multiple_monsters_var,
                                                              command=self.show_spinbox)
        self.checkbox_multiple_monsters.grid(row=0, column=0, sticky="W")

        self.spinbox_number_of_monsters = tkinter.Spinbox(
            App.frames['monster_frame'], from_=1, to=10, width=10)
        self.generate_monster()

        # Frame do Gerador de Ferimento
        App.frames['effect_frame'] = customtkinter.CTkFrame(
            main_container, fg_color='#000811')
        self.effectButton = customtkinter.CTkButton(
            App.frames['effect_frame'], text='Gerar', command=self.generate_effect_destiny)
        self.effectButton.pack(pady=20)

        self.effectResult = scrolledtext.ScrolledText(
            App.frames['effect_frame'])
        self.effectResult.configure(
            state='disabled', background='#000811', fg='white')
        self.effectResult.pack()

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=MONSTROS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def show_spinbox(self):
        if self.checkbox_multiple_monsters_var.get():
            self.spinbox_number_of_monsters.grid(row=0, column=0, padx=40)
            self.spinbox_number_of_monsters.configure(state='normal')
        else:
            self.spinbox_number_of_monsters.configure(state='disabled')
            self.spinbox_number_of_monsters.grid_forget()

    def generate_monster(self):
        for i, row in enumerate(self.table_entries, start=2):
            for j, entry in enumerate(row):
                entry.grid_forget()
                entry.destroy()

        self.table_entries = []
        quantity = 1
        if self.checkbox_multiple_monsters_var.get():
            quantity = int(self.spinbox_number_of_monsters.get())
        for _ in range(quantity):
            monster = random.choice(self.monsters.monster_table)
            nome, rank, quantidade, _ = monster
            if rank == 2 or rank == 3:
                quantidade = random.choices(
                    [1, 2], weights=[0.85, 0.15], k=1)[0]
                _ = self.loot_table.loot_table[random.randint(1, 3)]
            else:
                try:
                    quantidade = int(quantidade)
                except ValueError:
                    quantidade = 1
                quantidade = str(random.randint(1, quantidade))

                _ = self.loot_table.loot_table[random.randint(1, 3)]
            self.table_entries.append([
                tkinter.Entry(self.frame_generator_monster, width=22),
                tkinter.Entry(self.frame_generator_monster, width=22),
                tkinter.Entry(self.frame_generator_monster, width=22),
                tkinter.Entry(self.frame_generator_monster, width=22),
            ])
            self.table_entries[-1][0].insert(0, nome)
            self.table_entries[-1][1].insert(0, rank)
            self.table_entries[-1][2].insert(0, quantidade)
            self.table_entries[-1][3].insert(0, _)
            self.table_entries[-1][0].configure(state='disabled')
            self.table_entries[-1][1].configure(state='disabled')
            self.table_entries[-1][2].configure(state='disabled')
            self.table_entries[-1][3].configure(state='disabled')

        header = [tkinter.Entry(self.frame_generator_monster, width=22),    tkinter.Entry(self.frame_generator_monster, width=22),    tkinter.Entry(
            self.frame_generator_monster, width=22),    tkinter.Entry(self.frame_generator_monster, width=22),]
        header[0].insert(0, "Nome")
        header[1].insert(0, "Rank")
        header[2].insert(0, "Quantidade")
        header[3].insert(0, "Loot")

        for j, entry in enumerate(header):
            entry.grid(row=0, column=j)
        for i, row in enumerate(self.table_entries, start=1):
            for j, entry in enumerate(row):
                entry.grid(row=i, column=j)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=FEITIÇOS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Gerar a lista de feitiços
    def spell_list_func(self):
        self.list = self.spells.spellList['tipos']
        names = [n for n in self.spells.spellList['tipos']]
        for i in range(0, 6):
            self.spell_list.insert(
                tkinter.INSERT, f'-=-=-=-=-=-=-=-=-=-=-=-=-\nFeitiços de {names[i].capitalize()}\n-=-=-=-=-=-=-=-=-=-=-=-=-\n')
            for j in range(0, 6):
                self.nome = self.list[names[i]][j]['nome']
                self.tipo = self.list[names[i]][j]['tipo']
                self.duracao = self.list[names[i]][j]['duracao']
                self.efeito = self.list[names[i]][j]['efeito']
                self.mais_efeito = self.list[names[i]][j]['+20']
                if self.tipo == None:
                    self.tipo = ''
                if self.duracao == None:
                    self.duracao = ''
                if self.mais_efeito == None:
                    self.mais_efeito = ''
                self.spell_list.insert(
                    tkinter.INSERT, f'\nNome: {self.nome}\nTipo: {self.tipo}\nDuração: {self.duracao}\nEfeito: {self.efeito}\n+20: {self.mais_efeito}\n\n')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=LOOT-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Mostrar opção de bau
    def toggle_spinbox(self):
        if self.show_num_chests.get() == 'on':
            self.num_chests_spinbox.place(
                relx=0.26, rely=0.22, anchor='center')
        else:
            self.num_chests_spinbox.place_forget()

    # Gerador de loot
    def roll_dice(self):
        self.num_chests = int(self.num_chests_spinbox.get())
        result = []
        for i in range(self.num_chests):
            dice = int(self.effects.dices.get()[1:])
            roll = random.randint(1, 6)
            if roll == 5:
                item = self.loot_table.loot_table[roll]
                if type(item) is dict:
                    spell_choice = random.randint(1, 6)
                    spell = self.loot_table.loot_table[5]['feiticos'][spell_choice]
                    result.append(spell)
                else:
                    result.append(roll)
            elif roll == 6:
                item = self.loot_table.loot_table[roll]
                if type(item) is dict:
                    forma = random.randint(1, 20)
                    enchanted_item = self.enchanted_item.generate_enchanted_item(
                        self.loot_table.loot_table[6]['forma'][forma])
                    result.append(enchanted_item)
                else:
                    result.append(roll)
            else:
                result.append(self.loot_table.loot_table[roll])

        # Mostrar na tela o loot
        self.result_text.configure(state='normal')
        self.result_text.delete('1.0', tkinter.END)
        self.result_text.insert(tkinter.INSERT, '\n'.join(result))
        self.result_text.configure(
            state='disabled', background='#000811', fg='white')

        # Salvar no arquivo
        with open("loots.txt", "w") as f:
            f.write('Loots\n')
            f.write("\n".join(result))


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=EFEITOS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Gerar efeitos


    def generate_effect_destiny(self):
        self.result_effect = {'name': '', 'effect': '', 'description': ''}
        result = self.effects.dice(6)
        if result == 1:
            self.injury_table(4*result)
        elif result > 1 and result < 6:
            self.injury_table(3*result)
        else:
            self.result_effect['name'] = "Efeito Evitado"
            self.result_effect['effect'] = "Foi Por Pouco. O personagem conseguiu evitar o ferimento por pura sorte. Ele fica assustado por 1 rodada e precisa conseguir um sucesso em uma jogada de desafio de Agilidade ou derruba o que está segurando."
            self.result_effect['description'] = result

    def injury_table(self, dice):
        for key in self.effects.injury:
            if dice <= key:
                if key == 4:
                    self.knockout_injury()
                elif key == 5:
                    self.staggering_wound()
                elif key == 6:
                    self.traumatic_injury()
                elif key == 8:
                    self.painful_wound()
                elif key == 11:
                    self.minor_injury()
                elif key == 16:
                    self.bleeding_injury()
                elif key == 19:
                    self.crippled_injury()
                elif key == 21:
                    self.limb_lost()
                elif key == 22:
                    self.coma_injury()
                elif key == 23:
                    self.horrible_wound()
                else:
                    self.catastrophic_injury()

                # Mostrar na tela o efeito
                self.effectResult.configure(state='normal')
                self.effectResult.delete('1.0', tkinter.END)

                effect_dict = {
                    'name': self.result_effect.get('name'),
                    'effect': self.result_effect.get('effect'),
                    'description': self.result_effect.get('description')
                }
                if 'more_effect' in self.result_effect:
                    effect_dict['more_effect'] = self.result_effect.get(
                        'more_effect')
                if 'scar' in self.result_effect:
                    effect_dict['scar'] = self.result_effect.get('scar')
                if 'stats_effect' in self.result_effect:
                    effect_dict['stats_effect'] = self.result_effect.get(
                        'stats_effect')
                if 'body_limp' in self.result_effect:
                    effect_dict['body_limp'] = self.result_effect.get(
                        'body_limp')

                self.effectResult.insert(
                    tkinter.INSERT, f"Nome\n{effect_dict['name']}\n"
                                    f"\nEfeito\n{effect_dict['effect']}\n"
                                    f"\nDescrição\n{effect_dict['description']}\n")

                if 'more_effect' in effect_dict:
                    self.effectResult.insert(
                        tkinter.INSERT, f"\n\nMais Efeitos\n{effect_dict['more_effect']}\n")

                if 'scar' in effect_dict:
                    self.effectResult.insert(
                        tkinter.INSERT, f"\n\nCicatriz\n{effect_dict['scar']}\n")

                if 'stats_effect' in effect_dict:
                    self.effectResult.insert(
                        tkinter.INSERT, f"\n\nEfeito nas estatísticas\n{effect_dict['stats_effect']}\n")

                if 'body_limp' in effect_dict:
                    self.effectResult.insert(
                        tkinter.INSERT, f"\n\nMembro(s) perdido(s)\n{effect_dict['body_limp']}\n")

                self.effectResult.insert(
                    tkinter.INSERT, "\n")

                self.effectResult.configure(
                    state='disabled', background='#000811', fg='white')
                return

    def knockout_injury(self):
        dice = self.effects.dice(6)
        rounds = 1
        while dice % 2 != 0:
            rounds += 1
            dice = self.effects.dice(6)
        self.result_effect['name'] = self.effects.injury[4][0]
        self.result_effect['effect'] = f'Caiu prostrado, porém, removeu a aflição inconsciente. \n'
        self.result_effect['description'] = self.effects.injury[4][1]
        self.result_effect[
            'more_effect'] = f'Quantidade de Rodadas que o personagem ficou inconsciente: {rounds}'

    def staggering_wound(self):
        self.result_effect['name'] = self.effects.injury[5][0]
        self.result_effect['description'] = self.effects.injury[5][1]

    def traumatic_injury(self):
        insanity = self.effects.dice(3)
        scar = self.effects.get_scar()
        self.result_effect['name'] = self.effects.injury[6][0]
        self.result_effect['effect'] = f'Ao ver o seu proprio corpo horrivelmente ferido o personagem ganha {insanity} de insanidade. Enquanto permanecer assustado por ganhar Insanidade, o personagem também fica debilitado. \nCaso ele tente resistir a um ferimento traumático deixa uma cicatriz em algum lugar do corpo.'
        self.result_effect['description'] = self.effects.injury[6][1]
        self.result_effect['scar'] = f'{scar}'

    def painful_wound(self):
        self.result_effect['name'] = self.effects.injury[8][0]
        self.result_effect['description'] = self.effects.injury[8][1]

    def minor_injury(self):
        self.result_effect['name'] = self.effects.injury[11][0]
        self.result_effect['description'] = self.effects.injury[11][1]

    def bleeding_injury(self):
        self.result_effect['name'] = self.effects.injury[16][0]
        self.result_effect['description'] = self.effects.injury[16][1]

    def crippled_injury(self):
        results = self.effects.dice(6)
        membros = self.effects.table[results]
        self.result_effect['name'] = self.effects.injury[19][0]
        self.result_effect['description'] = self.effects.injury[19][1]
        self.result_effect['body_limp'] = f'{membros}'

    def limb_lost(self):
        dice = 2 * self.effects.dice(6)
        for key in self.effects.limb_table:
            if dice <= key:
                self.result_effect['name'] = self.effects.injury[21][0]
                self.result_effect['description'] = self.effects.injury[21][1]
                self.result_effect['body_limp'] = f'{self.effects.limb_table[key]}'

    def coma_injury(self):
        weeks = self.effects.dice(3)
        self.result_effect['name'] = self.effects.injury[22][0]
        self.result_effect['description'] = self.effects.injury[22][1]
        self.result_effect['more_effect'] = f'Semanas em coma: {weeks}'

    def horrible_wound(self):
        rounds = self.effects.dice(3)
        self.result_effect['name'] = self.effects.injury[23][0]
        self.result_effect['description'] = self.effects.injury[23][1]
        self.result_effect['more_effect'] = f'Rodadas: {rounds}'

    def catastrophic_injury(self):
        self.result_effect['name'] = self.effects.injury[24][0]
        self.result_effect['description'] = self.effects.injury[24][1]


a = App()
a.mainloop()
