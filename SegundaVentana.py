import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class SegundaVentana(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("VENTANA DE COLORES")
        principalBOX = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vBox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vBox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        # Llamamos  a la funcion buttonWithColor a la que le pasamos un color, esta funcion devuelve un boton del color que le hemos pasado

        # AÑADIMOS A LA CAJA 1 UN BOTON DE COLOR ROJO, UNO AMARILLO Y OTRO VERDE
        vBox1.pack_start(self.buttonWithColor("Red"), True, True, 5)  # El numero 5 es una especie de padding
        vBox1.pack_start(self.buttonWithColor("Yellow"), True, True, 5)  # el primer True es para que el boton se expanda al tamaño de la caja
        vBox1.pack_start(self.buttonWithColor("Green"), True, True,5)  # El segundo True es para que el boton se rellene

        # AHORA A LA SEGUNDA CAJA VAMOS A AÑADIR OTROS BOTONES DE COLORES
        vBox2.pack_start(self.buttonWithColor("Red"), True, True, 5)
        vBox2.pack_start(self.buttonWithColor("Purple"), True, True, 5)

        # AHORA AÑADIREMOS LAS CAJAS A LA PRINCIPAL MAS 1 BOTON
        principalBOX.pack_start(vBox1, True, True, 5)
        principalBOX.pack_start(self.buttonWithColor("Red"), True, True, 5)
        principalBOX.pack_start(vBox2, True, True, 5)

        self.add(principalBOX)

        # para los listeners/eventos
        self.connect("delete-event", Gtk.main_quit)  # sin los parentesis del método main_quit
        self.show_all()

    def on_debuxa(self, control, cr, datos):
        contexto = control.get_style_context()
        ancho = control.get_allocated_width()
        alto = control.get_allocated_height()
        Gtk.render_background(contexto, cr, 0, 0, ancho, alto)

        r, g, b, a = datos["color"]
        cr.set_source_rgba(r, g, b, a)
        cr.rectangle(0, 0, ancho, alto)
        cr.fill()

    def buttonWithColor(self, color):
        rgba = Gdk.RGBA()
        rgba.parse(color)

        boton = Gtk.Button()
        area = Gtk.DrawingArea()
        area.set_size_request(32, 24)
        area.connect("draw", self.on_debuxa, {"color": rgba})

        boton.add(area)
        return boton

        # button: sirve cualquier nombre para recoger una referencia al control que generó
        # la señal (el evento clicked), lo tiene que recibir SIEMPRE!!!


if __name__ == "__main__":
    SegundaVentana()  # nombre de tu clase
    Gtk.main()
