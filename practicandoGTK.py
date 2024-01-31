import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ventana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Practicando Ventana GTK")
        # contenedor de la ventana
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        image1 = Gtk.Image()
        image1.set_from_file("galaxy-brain-default.png")

        self.label = Gtk.Label(label="Esto es un label")

        # Linea de texto editable
        self.textEdit = Gtk.Entry()  # self indica que es una especie de variable publica

        # Creamos un boton
        btn_ok = Gtk.Button(label="Ok")
        btn_ok.connect("clicked", self)

        # Añadimos todos los elementos al box
        box.pack_start(image1, True, True, 0)
        box.pack_start(self.label, True, True, 0)
        box.pack_start(self.textEdit, True, True, 0)
        box.pack_start(btn_ok, True, True, 0)

        self.add(box)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


