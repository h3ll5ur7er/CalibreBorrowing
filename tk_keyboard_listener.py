from tkinter import *
from tkinter import ttk


class KeyboardListener:

    def _handle_keypress(self, evt):
        char = evt.char
        if char:
            self.buffer += char

    def _handle_enterpress(self, evt):
        self.enter_action(self.buffer)
        self.buffer = ""

    def _bind_key_listener(self, *a, **kw):
        self.window.bind("<Key>", self._handle_keypress)
        self.window.bind("<Return>", self._handle_enterpress)

    def _unbind_key_listener(self, *a, **kw):
        self.window.unbind_all("<Key>")
        self.window.unbind_all("<Return>")

    def __init__(self, window, enter_action):
        self.window = window
        self.enter_action = enter_action
        self.buffer = ""
        self.window.bind('<Enter>', self._bind_key_listener)
        self.window.bind('<Leave>', self._unbind_key_listener)
