import tkinter as tk
from aluno import Aluno

janela = tk.Tk()
A = Aluno()

def processar():
    A.cadastrar(entry_nome.get(), entry_sobrenome.get(), entry_idade.get(), entry_telefone.get())
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_idade.delete(0, "end")
    entry_telefone.delete(0, "end")

janela.title("Janela de cadastro")

label_nome = tk.Label(janela, text="Nome", fg="#5a3ac2" ,font=('arial', 12))
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text="Sobrenome", fg="#5a3ac2", font=('arial', 12))
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_idade = tk.Label(janela, text="Idade", fg="#5a3ac2", font=('arial', 12))
label_idade.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text="Telefone", fg="#5a3ac2", font=('arial', 12))
label_telefone.grid(row=3, column=0, padx=10, pady=10)


entry_nome = tk.Entry(janela, width=30)
entry_nome.grid (row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width=30)
entry_sobrenome.grid (row=1, column=1, padx=10, pady=10)

entry_idade = tk.Entry(janela, width=30)
entry_idade.grid (row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, width=30)
entry_telefone.grid (row=3, column=1, padx=10, pady=10)

entry_botao = tk.Button(janela, text="CADASTRAR", command=processar)
entry_botao.grid(row=4, column=1, padx=10, pady=10)


janela.mainloop()