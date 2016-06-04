import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Register import Register
from Status import Status


class RegisterPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.set_homogeneous(True)

        self.register = Register()
        self.add(self.register)

        self.status = Status()
        self.add(self.status)

