import gi
from statics import VERSION_CODE

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class ColoredButton(Gtk.Button):
    def override_color(*args, **kwargs):
        pass
# ok


class TrainingWindow:
    window = Gtk.Window()

    def __init__(self):
        pass

    def add_sentences(self, sentences: list[str]):
        for sentence in sentences:
            box = Gtk.Box(spacing=5)
            box.add(Gtk.CheckButton())
            box.add(Gtk.Label(label=sentence))
            self.boxes.add(box)
        submit = ColoredButton(label="Submit")
        self.boxes.add(submit)

    def show_window(self):
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)
        Gtk.main()

    window.set_title("Don't Read It {}".format(VERSION_CODE))
    window.resize(1080, 720)

    scroll = Gtk.ScrolledWindow()
    scroll.set_margin_left(10)
    scroll.set_margin_top(10)
    scroll.set_margin_bottom(10)
    scroll.set_margin_right(10)
    window.add(scroll)

    boxes = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    scroll.add(boxes)

    """
    item1 = Gtk.Button(label="KNOPF")
    boxes.add(item1)
    item2 = Gtk.Button(label="KNOPF 2")
    boxes.add(item2)
    for i in range(20):
        boxes.add(Gtk.Button(label="Knopf " + str(i)))
    """
