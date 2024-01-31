

from CreandoVentana import CreandoVentana
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
if __name__ == "__main__":
    CreandoVentana()  # nombre de tu clase
    Gtk.main()
