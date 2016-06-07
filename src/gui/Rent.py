import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Rent(Gtk.Box):
    def __init__(self, lib):
        Gtk.Box.__init__(self)

        self.library = lib

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("RENT")
        self.label2 = Gtk.Label(" ")

        self.customerBarcodeLabel = Gtk.Label("Customer barcode:")
        self.customerBarcode = Gtk.Entry()
        self.customerBarcode.set_max_length(8)

        self.volumeBarcodeLabel = Gtk.Label("Volume barcode:")
        self.volumeBarcode = Gtk.Entry()
        self.volumeBarcode.set_max_length(8)

        self.buttonLabel = Gtk.Label(" ")
        self.button = Gtk.Button(label="RENT")
        self.button.connect("clicked", self.rentBook)

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        # self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.customerBarcodeLabel, False, True, padding)
        self.labelBox.pack_start(self.volumeBarcodeLabel, False, True, padding)
        self.labelBox.pack_start(self.buttonLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.customerBarcode, False, False, 0)
        self.valuesBox.pack_start(self.volumeBarcode, False, False, 0)
        self.valuesBox.pack_start(self.button, False, False, 0)

    def rentBook(self, button):
        customerBarcode = int(self.customerBarcode.get_text())
        volumeBarcode = int(self.volumeBarcode.get_text())
        self.library.loans.rentBook(parameters=(customerBarcode, volumeBarcode))
