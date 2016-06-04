import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Status(Gtk.ScrolledWindow):
    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)

        self.set_vexpand(True)

        self.textView = Gtk.TextView()
        self.textView.set_editable(False)
        self.textView.set_cursor_visible(False)
        self.textView.set_wrap_mode(True)

        self.textView.set_justification(Gtk.Justification.LEFT)
        self.textView.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 65535, 65535))
        # self.set_size_request(-1, 250)

        self.add(self.textView)
