from os.path import exists

import gi

import regression_calc
import vector_creator
from statics import VERSION_CODE

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class TrainingWindow:
    window = Gtk.Window()
    result = ""
    sentence_list = []
    weights = []
    callback = 0

    def __init__(self, weights: list, callback):
        self.weights = weights
        self.callback = callback

    def add_sentences(self, sentences: list[str]) -> list[Gtk.CheckButton]:
        self.sentence_list = sentences
        check_boxes = []
        for sentence in sentences:
            box = Gtk.Box(spacing=5)
            label = Gtk.Label(label=sentence)
            check_box = Gtk.CheckButton()
            label_box = Gtk.EventBox()
            label_box.connect("button-press-event", self.box_clicked, check_box)
            label_box.add(label)
            box.add(check_box)
            box.add(label_box)
            self.boxes.add(box)
            check_boxes.append(check_box)
        button_box = Gtk.Box(spacing=10)
        submit = Gtk.Button(label="Submit")
        submit.get_style_context().add_class("green")
        submit.connect("clicked", self.submit, check_boxes)
        reset = Gtk.Button(label="Reset")
        reset.get_style_context().add_class("red")
        reset.connect("clicked", self.uncheck_all, check_boxes)
        button_box.add(submit)
        button_box.add(reset)
        self.boxes.add(button_box)
        return check_boxes

    def box_clicked(self, widget, event, check_box: Gtk.CheckButton):
        check_box.set_active(not check_box.get_active())

    def uncheck_all(self, b, check_boxes: list[Gtk.CheckButton]):
        for button in check_boxes:
            button.set_active(False)

    def submit(self, b, check_boxes: list[Gtk.CheckButton]):
        for i in range(len(self.sentence_list)):
            creator = vector_creator.VectorCreator(self.sentence_list[i])
            sentence_vec = creator.create_sentence_vec()
            s = regression_calc.sigmoid(sentence_vec, self.weights)
            self.weights = regression_calc.update_weights(sentence_vec, self.weights, s, check_boxes[i].get_active())
        self.callback(self.weights)
        Gtk.main_quit()

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

    if exists("styles.css"):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("./styles.css")
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    """
    item1 = Gtk.Button(label="KNOPF")
    boxes.add(item1)
    item2 = Gtk.Button(label="KNOPF 2")
    boxes.add(item2)
    for i in range(20):
        boxes.add(Gtk.Button(label="Knopf " + str(i)))
    """
