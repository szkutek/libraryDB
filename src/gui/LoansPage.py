import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Rent import Rent
from Return import Return
from Status import Status

class LoansPage(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.set_row_spacing(5)
        self.set_column_spacing(20)

        self.rents = Rent()
        self.returns = Return()
        self.status = Status()

        self.attach(self.rents, 0, 0, 1, 1)
        self.attach(self.returns, 0, 1, 1, 1)
        self.attach(self.status, 1, 1, 1, 2)
