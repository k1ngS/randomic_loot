import tkinter as tk
import customtkinter


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configuração do app
        self.width = 800
        self.height = int(0.618 * self.width)
        self.title('Loot Generator')
        self.geometry("{}x{}".format(self.width, self.height))
        self.resizable(False, False)

        self.set_appearance_mode('dark')
        self.set_default_color_theme('blue')

        # Criação da sidebar
        self.sidebar = customtkinter.CTkFrame(
            self, width=100, height=500)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Adição de botões à sidebar
        self.button1 = customtkinter.CTkButton(self.sidebar, text="Loot")
        self.button1.pack(pady=30, fill=tk.BOTH)
        self.button2 = customtkinter.CTkButton(
            self.sidebar, text="Lista de Feitiços")
        self.button2.pack(fill=tk.BOTH)

        # Criação do Header
        self.header_frame = customtkinter.CTkFrame(
            self, height=60)
        self.header_frame.pack(side='top', fill='both')

        # Criação do conteúdo principal
        self.main_frame = customtkinter.CTkFrame(
            self, width=600, height=400)
        self.main_frame.pack(side='right', expand=True, fill='both')

        # Criando opções de dados
        self.dice_options = [("D6", 6), ("D8", 8),
                             ("D10", 10), ("D12", 12), ("D20", 20)]

        # Criando spinbox para escolha de quantidade dos baus
        self.num_chests = tk.IntVar()
        self.num_chests.set(0)
        self.num_chests_spinbox = tk.Spinbox(
            self.header_frame, from_=1, to=100, textvariable=self.num_chests)

        # Criando checkbox para habilitar ou desabilitar o spinbox
        self.show_num_chests = tk.IntVar()
        self.show_num_chests_checkbox = tk.Checkbutton(
            self.header_frame, text="+bau?", variable=self.show_num_chests, command=self.toggle_spinbox)

        # Criando botão para gerar loot
        self.generate_button = customtkinter.CTkButton(
            self.header_frame, text="Gerar loot", command=self.generate_loot)

        # Criando opções de dados como botões de radio
        self.dice = tk.IntVar()
        self.dice.set(6)
        self.dice_buttons = []
        for i, (dices, sides) in enumerate(self.dice_options):
            b = tk.Radiobutton(self.header_frame, text=dices, variable=self.dice,
                               value=sides, command=self.select_dice)
            self.dice_buttons.append(b)

        self.show_num_chests_checkbox.pack(
            side='left', padx=(50, 0), pady=(15, 15), anchor='nw')
        self.generate_button.pack(side='right', padx=(
            0, 30), pady=(15, 15), anchor='nw')
        for b in self.dice_buttons:
            b.pack(side='right',
                   padx=(0, 15), pady=(15, 15), anchor='nw')

    def toggle_spinbox(self):
        if self.show_num_chests.get() == 1:
            self.num_chests_spinbox.pack(
                side='left', padx=(20, 0), pady=(18, 0), anchor='nw')
        else:
            self.num_chests_spinbox.pack_forget()

    def select_dice(self):
        pass

    def generate_loot(self):
        pass


app = Main()
app.mainloop()
