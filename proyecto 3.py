#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *               # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading
import pickle                       # 
import os                           # ruta = os.path.join('')
import time                         # time.sleep(x)
from tkinter import messagebox      # AskYesNo ()
import tkinter.scrolledtext as tkscrolled
##### Biblioteca para el Carro
from WiFiClient import NodeMCU


class venprincipal:

    def __init__(self):
        
        self.venprincipal = Tk()
        self.venprincipal.title('Proyecto 3')
        self.venprincipal.minsize(1000,700)
        self.venprincipal.resizable(width=NO,height=NO)
        self.fondo1=PhotoImage(file="carro vista.png")
        self.lblfondo1 = Label(self.venprincipal,image=self.fondo1).place(x=0,y=0)

    def openvesc(self):
        venverescuderia = ver
        venverescuderia.ver()
        
    def openpiloto(self):
        venopenpiloto = venpiloto
        venopenpiloto.venpiloto()

    def openabout(self):
        venopenabout = Venabout
        venopenabout.Venabout()

    def opencesc(self):
        venopencesc = crear
        venopencesc.crear()

    def salir():
        venprincipal.destroy()

    def setMainloop(self):
        self.venprincipal.mainloop()
        
    def botones(self):    

        self.verEscuderias = Button(self.venprincipal,text='Ver Escuderias',command=lambda:openvesc(None),fg='white',bg='blue', font=('Agency FB',12))
        self.verEscuderias.place(x=200,y=100)

        self.Pilotos = Button(self.venprincipal,text='Ingresar Pilotos',command=lambda:openpiloto(None),fg='white',bg='blue', font=('Agency FB',12))
        self.Pilotos.place(x=100,y=100)

        self.AboutBtn = Button(self.venprincipal,text='About',command=lambda:openabout(None),fg='white',bg='blue', font=('Agency FB',12))
        self.AboutBtn.place(x=100,y=100)

        self.crearEscuderias = Button(self.venprincipal,text='Crear Escuderias',command=lambda:opencesc(None),fg='white',bg='blue', font=('Agency FB',12))
        self.crearEscuderias.place(x=100,y=100)

        self.salirBtn = Button(self.venprincipal,text="SALIR",command=lambda:salir(None),fg="red",bg= "Grey")
        self.salirBtn.place(x=360,y=500)

class VenAbout:
    
    def __init__(self):
        self.venabout=Toplevel()
        self.venprincipal.withdraw()
        self.crear.withdraw()
        self.ver.withdraw()
        self.about.withdraw()
        self.venabout.title('About')
        self.venabout.minsize(1000,700)
        self.venabout.resizable(width=NO,height=NO)
        
class Escuderias:

    def ver(self):
        self.venver=Toplevel()
        self.venprincipal.withdraw()
        self.crear.withdraw()
        self.ver.withdraw()
        self.about.withdraw()
        self.venver.title('Ver Piloto')
        self.venver.minsize(1000,700)
        self.venver.resizable(width=NO,height=NO)

    def crear(self):
        self.vencrear=Toplevel()
        self.venprincipal.withdraw()
        self.crear.withdraw()
        self.ver.withdraw()
        self.about.withdraw()
        self.vencrear.title('Crear Piloto')
        self.vencrear.minsize(1000,700)
        self.vencrear.resizable(width=NO,height=NO)
        
class VenPilotos:

    def __init__(self):
        self.venpiloto=Toplevel()
        self.venprincipal.withdraw()
        self.crear.withdraw()
        self.ver.withdraw()
        self.about.withdraw()
        self.venpiloto.title('Piloto')
        self.venpiloto.minsize(1000,700)
        self.venpiloto.resizable(width=NO,height=NO)


main = venprincipal()
main.setMainloop()
    



#import pickle
#args=["1","2","3","3"]
#def ingresar_datos():
   # print('Ingresar cedula:')
   # ced = input()
   # write(ced)
# Store data (serialize)
#def write(cedula):
    #list_read=read()
    #list_read[cedula]=args
    #with open('filename.pickle', 'wb') as handle:
        #pickle.dump(list_read, handle, protocol=pickle.HIGHEST_PROTOCOL)
# Load data (deserialize)
#def read():
    #with open('filename.pickle', 'rb') as handle:
        #unserialized_data = pickle.load(handle)
    #return unserialized_data

######################################################

#def toggle_entry():
    #global hidden
    #if hidden:
        #e.grid()
    #else:
        #e.grid_remove()
    #hidden = not hidden

#hidden = False
#root = tk.Tk()
#e = tk.Entry(root)
#e.grid(row=0, column=1)
#tk.Button(root, text='Toggle entry', command=toggle_entry).grid(row=0, column=0)
#root.mainloop()
