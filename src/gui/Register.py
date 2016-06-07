import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Register(Gtk.Box):
    def __init__(self, lib):
        Gtk.Box.__init__(self)

        self.library = lib

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label()
        self.label.set_markup("<b>REGISTER NEW CUSTOMER</b>")
        self.label2 = Gtk.Label(" ")

        self.nameLabel = Gtk.Label("Name:")
        self.name = Gtk.Entry()
        self.name.set_max_length(40)

        self.addressLabel = Gtk.Label("Address:")
        self.address = Gtk.Entry()
        self.address.set_max_length(100)

        self.birthDateLabel = Gtk.Label("Birth date:")
        self.birthDate = Gtk.Entry()

        self.phoneNoLabel = Gtk.Label("Phone number:")
        self.phoneNo = Gtk.Entry()
        self.phoneNo.set_max_length(11)

        self.emailLabel = Gtk.Label("Email address:")
        self.email = Gtk.Entry()
        self.email.set_max_length(40)

        self.barcodeLabel = Gtk.Label("Customer barcode:")
        self.barcode = Gtk.Entry()
        self.barcode.set_max_length(8)

        self.buttonLabel = Gtk.Label(" ")
        self.button = Gtk.Button(label="REGISTER")
        self.button.connect("clicked", self.registerCustomer)

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        # self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.nameLabel, False, True, padding)
        self.labelBox.pack_start(self.addressLabel, False, True, padding)
        self.labelBox.pack_start(self.birthDateLabel, False, True, padding)
        self.labelBox.pack_start(self.phoneNoLabel, False, True, padding)
        self.labelBox.pack_start(self.emailLabel, False, True, padding)
        self.labelBox.pack_start(self.barcodeLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.name, False, False, 0)
        self.valuesBox.pack_start(self.address, False, False, 0)
        self.valuesBox.pack_start(self.birthDate, False, True, 0)
        self.valuesBox.pack_start(self.phoneNo, False, False, 0)
        self.valuesBox.pack_start(self.email, False, False, 0)
        self.valuesBox.pack_start(self.barcode, False, False, 0)
        self.valuesBox.pack_start(self.button, False, False, 0)

    def registerCustomer(self, button):
        name = str(self.name.get_text())
        address = str(self.address.get_text())
        birthDate = str(self.birthDate.get_text())
        phoneNo = int(self.phoneNo.get_text())
        email = str(self.email.get_text())
        barcode = str(self.barcode.get_text())

        self.library.customer.register(parameters=(barcode, name, address, birthDate, phoneNo, email))
