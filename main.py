

from CreandoVentana import CreandoVentana
import gi

from SegundaVentana import SegundaVentana

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
if __name__ == "__main__":
    SegundaVentana()  # nombre de tu clase
    Gtk.main()
