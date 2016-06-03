import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Lend(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("LEND")
        self.label2 = Gtk.Label(" ")

        self.nameLabel = Gtk.Label("Customer barcode:")
        self.name = Gtk.Entry()
        # self.name.set_max_length(8)

        self.addressLabel = Gtk.Label("Volume barcode:")
        self.address = Gtk.Entry()
        # self.address.set_max_length(8)

        self.buttonLabel = Gtk.Label(" ")
        self.button = Gtk.Button(label="LEND")

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        # self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.nameLabel, False, True, padding)
        self.labelBox.pack_start(self.addressLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.name, False, False, 0)
        self.valuesBox.pack_start(self.address, False, False, 0)
