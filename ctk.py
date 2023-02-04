import tkinter
import customtkinter
import random

from tkinter import scrolledtext

from lootTable import LootTable
from enchantedItem import EnchantedItem

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')


class App(customtkinter.CTk):

    frames = {'main_frame': None, 'spell_frame': None}

    def main_frame_selector(self):
        App.frames['spell_frame'].pack_forget()
        App.frames['main_frame'].pack(
            in_=self.right_side_container, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=(100, 0))
        self.bt_from_main_frame.place(
            in_=self.right_side_container, relx=0.85, rely=0.22, anchor='center')
        self.dices.place(in_=self.right_side_container,
                         relx=0.85, rely=0.08, anchor='center')
        self.show_num_chests_checkbox.place(
            in_=self.right_side_container, relx=0.12, rely=0.22, anchor='center')

    def spell_frame_selector(self):
        App.frames['main_frame'].pack_forget()
        self.bt_from_main_frame.place_forget()
        self.dices.place_forget()
        self.show_num_chests_checkbox.place_forget()
        App.frames['spell_frame'].pack(
            in_=self.right_side_container, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def __init__(self):
        super().__init__()
        self.loot_table = LootTable()
        self.enchanted_item = EnchantedItem()

        self.title('Loot Generator')
        self.geometry('800x400')
        self.resizable(False, False)

        main_container = customtkinter.CTkFrame(self)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # Sidebar + buttões
        left_side_panel = customtkinter.CTkFrame(main_container, width=150)
        left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y,
                             expand=False, padx=10, pady=10)

        bt_main_frame = customtkinter.CTkButton(
            left_side_panel, text='Loot', command=self.main_frame_selector)
        bt_main_frame.grid(row=0, column=0, padx=20, pady=10)

        bt_spell_frame = customtkinter.CTkButton(
            left_side_panel, text='Spell List | DISABLED', command=self.spell_frame_selector, state=tkinter.DISABLED)
        bt_spell_frame.grid(row=1, column=0, padx=20, pady=10)

        myCredits = customtkinter.CTkLabel(
            left_side_panel, text='created by k1ngS')
        myCredits.grid(row=10, column=0, pady=240)

        # Criando painel direito para ficar alojado os Frames Principais
        self.right_side_panel = customtkinter.CTkFrame(main_container)
        self.right_side_panel.pack(
            side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.right_side_container = customtkinter.CTkFrame(
            self.right_side_panel, fg_color="#000811")
        self.right_side_container.pack(
            side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # Criando Frame de Loot
        App.frames['main_frame'] = customtkinter.CTkFrame(
            main_container)
        self.bt_from_main_frame = customtkinter.CTkButton(
            main_container, text='Gerar Loot', command=self.roll_dice)
        self.bt_from_main_frame.place_forget()

        # Criando combox dos dados de d6 até d20
        self.dices = customtkinter.CTkOptionMenu(
            main_container, values=['D6', 'D8', 'D10', 'D12', 'D20'])
        self.dices.place_forget()

        # Criando checkbox dos baus
        self.show_num_chests = tkinter.StringVar()
        self.show_num_chests_checkbox = customtkinter.CTkCheckBox(
            master=main_container, text='+bau?', command=self.toggle_spinbox, variable=self.show_num_chests, onvalue='on', offvalue='off')
        self.show_num_chests_checkbox.place_forget()

        # Criando spinbox dos baus
        self.num_chests = tkinter.IntVar()
        self.num_chests.set(1)
        self.num_chests_spinbox = tkinter.Spinbox(
            self.right_side_container, from_=1, to=100, width=5, textvariable=self.num_chests)

        # # Criando Resultado dos Loots
        # self.result_label = tkinter.Label(
        #     App.frames['main_frame'], text='Loot', wraplength=300)
        # self.result_label.pack(fill=tkinter.BOTH, expand=True)

        # Criando scrollbar
        # self.result_text = tkinter.Text(
        #     App.frames['main_frame'], wrap='word')
        # self.result_text.pack(fill=tkinter.BOTH, expand=True)
        self.result_text = scrolledtext.ScrolledText(
            App.frames['main_frame'])
        self.result_text.configure(
            state='disabled', background='#000811', fg='white')
        self.result_text.pack()

        # Criando Frame da Lista de Spells
        App.frames['spell_frame'] = customtkinter.CTkFrame(
            main_container, fg_color='blue')
        self.bt_from_spell_frame = customtkinter.CTkButton(
            App.frames['spell_frame'], text='Spell List')
        self.bt_from_spell_frame.place(relx=0.5, rely=0.5, anchor='center')

    def toggle_spinbox(self):
        if self.show_num_chests.get() == 'on':
            self.num_chests_spinbox.place(
                relx=0.26, rely=0.22, anchor='center')
        else:
            self.num_chests_spinbox.place_forget()

    def roll_dice(self):
        self.num_chests = int(self.num_chests_spinbox.get())
        result = []
        for i in range(self.num_chests):
            dice = int(self.dices.get()[1:])
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

        self.result_text.configure(state='normal')
        self.result_text.delete('1.0', tkinter.END)
        self.result_text.insert(tkinter.INSERT, '\n'.join(result))
        self.result_text.configure(
            state='disabled', background='#000811', fg='white')
        with open("loots.txt", "w") as f:
            f.write('Loots\n')
            f.write("\n".join(result))


a = App()
a.mainloop()
