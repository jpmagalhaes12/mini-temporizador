from tkinter import *
from time import sleep


def iniciar():
   """
   Inicia o contador e para quando ele chega a 0.
   """
   global cont
   global rodar
   rodar = 0
   cont = int(tempo.get())
   while True:
       mover()
       if cont == 0:
           break
       cont -= 1
       sleep(1)


def mover():
    """
    move o relogio de acordo com o tempo passado. Quando terminar ele mostra
    uma mensagem.
    """
    global rodar
    global cont
    canvas.delete('seta', 'final', 'texto')
    rodar += (359 / (int(tempo.get())+1))
    seta = canvas.create_arc(105, 20, 275, 180, fill='light green',
                              width=4, tags='seta', extent=rodar)
    if cont == 0:
        tempo.delete(0, END)
        canvas.delete('seta')
        canvas.create_oval(105, 20, 275, 180, fill='light green', width=4, tags='final')
        canvas.create_text(190, 100, text="   TEMPO\nESGOTADO",
                            font=('futura', 15), fill='black', tags='texto')
    canvas.update()


rodar = 0
cont = 0
janela = Tk()
janela.geometry("380x300")
janela.title("Temporizador")
janela.config(bg='white')
janela.resizable(False, False)
canvas = Canvas(janela, height=200, width=380, bg='white')
canvas.pack()
relogio = canvas.create_oval(105, 20, 275, 180, fill='white', width=4)
ponto = canvas.create_oval(185, 95, 195, 104, fill='#555a57', outline='#555a57')
seta = canvas.create_arc(105, 20, 275, 180, fill='light green',
                          width=4, tags='seta', style=PIESLICE, extent=0)
label = Label(janela, height=10, width=55, bg='black')
label.pack()

tempo = Entry(label, font=('Arial', 20))
tempo.place(x=160, y=5, width=50, height=40)
enviar = Button(label, text="iniciar", width=6, bg='black', fg='#bdc8d6', relief='raised',
                font=('Verdana', 12), command=iniciar)
enviar.place(x=150, y=50)
janela.mainloop()
