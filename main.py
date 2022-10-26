from tkinter import *
from tkinter import ttk

import descripta
import encripta

root = Tk()
root.title("Crypto descktop n2")
root.geometry("600x100")

frm = ttk.Frame(root, padding=5)
frm.grid(row=10, column=1)


def encryptMessage():
    texto = encriptar_input.get()

    print("TESTE: ", texto)

    ct = encripta.encriptar_cesar(texto, 4)
    encriptado_input.insert(0, ct)


def decryptMessage():
    texto_cifrado = descriptar_input.get()

    resultado_descript = descripta.decriptar_cesar(texto_cifrado, 4)
    descriptado_input.insert(0, resultado_descript)



Label(frm, text='Texto a encriptar: ').grid(row=10, column=1)
encriptar_input = Entry(root)
encriptar_input.grid(row=10, column=2)

Label(root, text='Texto encriptado: ').grid(row=11, column=1)
encriptado_input = Entry(root)
encriptado_input.grid(row=11, column=2)

encriptar_botao = Button(root, text = "Encriptar", bg ="red", fg ="white", command=encryptMessage)
encriptar_botao.grid(row=13, column=2)


Label(root, text='Texto cifrado: ').grid(row=10, column=10)
descriptar_input = Entry(root)
descriptar_input.grid(row=10, column=11)


Label(root, text='Texto descriptado: ').grid(row=11, column=10)
descriptado_input = Entry(root)
descriptado_input.grid(row=11, column=11)

descriptar_botao = Button(root, text = "Descriptar", bg ="green", fg ="white", command=decryptMessage)
descriptar_botao.grid(row=13, column=11)


root.mainloop()
