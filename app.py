import tkinter as tk
import tkinter.ttk as ttk
import tkinter.simpledialog
import tkinter.messagebox
import os

class app_anotações:
    def __init__(self, master):
        self.master = master
        master.title("Degusta")

        # Visual
        self.style = ttk.Style(master)
        self.style.theme_use('alt')
        self.style.configure('TLabel', font=('Arial', 14))
        self.style.configure('TEntry', font=('Arial', 14))
        self.style.configure('TButton', font=('Arial', 14))

        # Informações       
        self.label1 = tk.Label(master, text="Nome Vinho")
        self.label1.grid(row=0, column=0, pady=5)

        self.label2 = tk.Label(master, text="Tipo da Uva")
        self.label2.grid(row=1, column=0, pady=5)

        self.label3 = tk.Label(master, text="Safra")
        self.label3.grid(row=2, column=0, pady=5)

        self.label4 = tk.Label(master, text="Comentários")
        self.label4.grid(row=3, column=0, pady=5)

        # campos de informações
        self.entry1 = tk.Entry(master, width=30)
        self.entry1.grid(row=0, column=1, pady=5)

        self.entry2 = tk.Entry(master, width=30)
        self.entry2.grid(row=1, column=1, pady=5)

        self.entry3 = tk.Entry(master, width=30)
        self.entry3.grid(row=2, column=1, pady=5)

        self.entry4 = tk.Text(master, height=10, width=30, font=('Arial', 14))
        self.entry4.grid(row=3, column=1, pady=5)

        # botões
        self.save_button = tk.Button(master, text="Salvar", command=self.save_notes)
        self.save_button.grid(row=4, column=1, pady=5)

        self.search_button = tk.Button(master, text="Consultar", command=self.search_notes)
        self.search_button.grid(row=4, column=0, pady=5)

    def save_notes(self):
        # recebe as informações inseridas
        Nome_Vinho = self.entry1.get()
        Tipo_da_Uva = self.entry2.get()
        Safra = self.entry3.get()
        Comentários = self.entry4.get("1.0", "end-1c")

        # grava os comentários na base de dados
        with open("Base.txt", "a") as f:
            f.write(f"Nome do Vinho: {Nome_Vinho}\n")
            f.write(f"Tipo da Uva: {Tipo_da_Uva}\n")
            f.write(f"Safra : {Safra}\n")
            f.write(f"Comentários: {Comentários}\n\n")

        # limpa as informações inseridas ao salvar
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete("1.0", tk.END)

    def search_notes(self):
        reference = tk.simpledialog.askstring("Referência", "Digite a referência da anotação:")
        with open("Base.txt", "r") as f:
            notes = f.read()
        if reference in notes:
            tk.messagebox.showinfo("Anotação encontrada", notes[notes.index(reference):notes.index("\n\n", notes.index(reference))])
        else:
            tk.messagebox.showerror("Anotação não encontrada", f"A referência '{reference}' não foi encontrada na base de anotações.")

root = tk.Tk()
my_app = app_anotações(root)
root.mainloop()