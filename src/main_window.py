import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="SVG Viewer")
        self.set_default_size(400, 300)

        # Load the SVG file into a GdkPixbuf.Pixbuf object
        svg_file = '/home/jeremi360/DevProjects/Python/Inkblend/src/test.svg'
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(svg_file)

        # Create a Gtk.Image widget to display the SVG
        image = Gtk.Image()
        image.set_from_pixbuf(pixbuf)

        # Add the Gtk.Image widget to the main window
        self.add(image)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
