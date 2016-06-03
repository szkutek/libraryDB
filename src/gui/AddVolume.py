import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AddVolume(Gtk.Box):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("ADD VOLUME")
        self.label2 = Gtk.Label(" ")

        self.isbnLabel = Gtk.Label("Enter ISBN:")
        self.isbn = Gtk.Entry()
        self.isbn.set_max_length(13)

        self.volumeBarcodeLabel = Gtk.Label("Volume barcode:")
        self.volumeBarcode = Gtk.Entry()
        self.volumeBarcode.set_max_length(8)

        self.buttonAddVolume = Gtk.Button(label="ADD VOLUME")

        padding = 7
        self.volumeLabelBox = Gtk.VBox(spacing=9)
        self.add(self.volumeLabelBox)
        self.volumeLabelBox.pack_start(self.label, False, False, padding)
        self.volumeLabelBox.pack_start(self.isbnLabel, False, False, padding)
        self.volumeLabelBox.pack_start(self.volumeBarcodeLabel, False, False, padding)

        self.volumeBox = Gtk.VBox(spacing=10)
        self.add(self.volumeBox)
        self.volumeBox.pack_start(self.label2, False, False, padding)
        self.volumeBox.pack_start(self.isbn, False, False, 0)
        self.volumeBox.pack_start(self.volumeBarcode, False, False, 0)
        self.volumeBox.pack_start(self.buttonAddVolume, False, False, 0)
