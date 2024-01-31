##Lo primero siempre es importar GTK para pdder trabaja rcon esta librería
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class CreandoVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        #Dentro del constructor es dond eguardamos los valores de la ventana

        #titulo
        self.set_title("TITULO DE LA VENTANA")

        #CONTENEDOR DE LOS ELEMENTOS DE LA VENTANA
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)

        #Ahora crearemos los elementos que finalmente añadiremos al box

        img = Gtk.Image()#creamos el elemento imagen, despues hay que añadir la imagen
        img.set_from_file("galaxy-brain-default.png")

        #Creamos un label
        self.label1 = Gtk.Label(label="ESTO ES UN LABEL EN LA VENTANA")#self se utiliza para poderlo usar en toda la clase

        #CREAMOS UNA LINEA DE TEXTO EDITABLE
        self.txt1 = Gtk.Entry()

        #Creamos un Botón
        self.btn1 = Gtk.Button(label="Esto es un botón")
        self.btn1.connect("clicked",self.on_click)

        ##finalmente devemos añadir los elementos al contenedor principal

        box.pack_start(img,True,True,0)
        box.pack_start(self.label1,True,True,0)
        box.pack_start(self.txt1,True,True,0)
        box.pack_start(self.btn1,True,True,0)

        #Ahora añadimos este contenedor con todos los elementos a la ventana

        self.add(box)
        self.connect("delete-event" , Gtk.main_quit)
        self.show_all()

    def on_click(self, d):
        print(self.txt1.get_text())

if __name__ == "__main__":
    CreandoVentana()  # nombre de tu clase
    Gtk.main()
