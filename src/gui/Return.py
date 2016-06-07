import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Return(Gtk.Box):
    def __init__(self, lib):
        Gtk.Box.__init__(self)
        self.set_spacing(10)
        self.set_border_width(10)
        # self.set_homogeneous(True)

        self.library = lib

        self.label = Gtk.Label("RETURN")
        self.label2 = Gtk.Label(" ")

        self.volumeBarcodeLabel = Gtk.Label("Volume barcode:")
        self.volumeBarcode = Gtk.Entry()
        # self.volumeBarcode.set_max_length(8)

        self.button = Gtk.Button(label="Return")
        self.button.connect("clicked", self.returnBook)

        padding = 7
        self.labelBox = Gtk.VBox(spacing=10)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.volumeBarcodeLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.volumeBarcode, False, False, 0)
        self.valuesBox.pack_start(self.button, False, False, 0)

    def returnBook(self, button):
        volumeBarcode = str(self.volumeBarcode.get_text())
        self.library.loans.returnBook(parameters=volumeBarcode)
