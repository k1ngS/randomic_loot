import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configuração do app
        self.title('Loot Generator')
        self.geometry("800x400")
        self.resizable(False, False)

        # Configuração da grid (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Criação da sidebar com widget
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text='Menu', font=customtkinter.CTkFont(size=20, weight='bold'))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_frame, text='Loot')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_frame, text='Spells')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text='Light/Dark Mode', anchor='w')
        self.appearance_mode_label.grid(row=5, column=0, padx=20)
        self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[
            'Light', 'Dark', 'System'], command=self.change_appearance_mode_event)

        self.appearance_mode_option_menu.grid(
            row=6, column=0, padx=20)
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text='UI Scale', anchor='w')
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_label_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[
            '80%', '90%', '100%', '110%', '120%'], command=self.change_scaling_event)

        self.scaling_label_option_menu.grid(
            row=8, column=0, padx=20, pady=(0, 20))

        # Opções para gerar loot
        self.main_button = customtkinter.CTkButton(
            master=self, fg_color='transparent', text='Gerar Loot', border_width=2, text_color=('gray10', '#DCE4EE'))
        self.main_button.grid(row=0, column=2, padx=(20, 20))

        # Valores Padrões
        self.appearance_mode_option_menu.set('Dark')
        self.scaling_label_option_menu.set('100%')

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace('%', '')) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == '__main__':
    app = Main()
    app.mainloop()
