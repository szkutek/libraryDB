import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Return(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("RETURN")
        self.label2 = Gtk.Label("     ")

        self.volumeBarcodeLabel = Gtk.Label("Volume barcode:")
        self.volumeBarcode = Gtk.Entry()
        # self.volumeBarcode.set_max_length(8)

        self.button = Gtk.Button(label="Return")

        self.labelBox = Gtk.Box(spacing=10)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label2, False, False, 0)
        self.labelBox.pack_start(self.label, False, False, 0)

        self.volumeBox = Gtk.Box(spacing=10)
        self.add(self.volumeBox)
        self.volumeBox.pack_start(self.volumeBarcodeLabel, False, True, 0)
        self.volumeBox.pack_start(self.volumeBarcode, False, False, 0)
        self.volumeBox.pack_start(self.button, False, False, 0)
