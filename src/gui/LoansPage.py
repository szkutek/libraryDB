import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Rent import Rent
from Return import Return
from Status import Status


class LoansPage(Gtk.VBox):
    def __init__(self, lib):
        Gtk.VBox.__init__(self)
        self.set_spacing(10)
        self.set_border_width(10)

        self.library = lib

        self.set_homogeneous(True)

        self.rents = Rent(self.library)
        self.returns = Return(self.library)
        self.status = Status()

        self.loansBox = Gtk.Box()
        self.add(self.loansBox)
        self.loansBox.add(self.rents)
        self.loansBox.add(self.returns)

        self.add(self.status)
