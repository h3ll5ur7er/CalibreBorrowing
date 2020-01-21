from tkinter import *
from tkinter import ttk
from tk_scroll_frame import VerticalScrolledFrame


class Table(VerticalScrolledFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def set_columns(self, columns):
        self.columns = columns
    def set_names(self, names):
        self.names = names
    def refresh(self, data):
        ## header
        for x, column in enumerate(self.names):
            Label(self.interior, text=column, relief=SUNKEN, font='Helvetica 10 bold', bg="#999999").grid(row=0, column=x, sticky="nsew")
        ## rows
        for y, row_id in enumerate(data):
            row = data[row_id]
            for x, column in enumerate(self.columns):
                if column == self.columns[0]:
                    value = row_id
                else:
                    value = row.get(column, "")
                Label(self.interior, relief=SUNKEN, text=value, font='Helvetica 10').grid(row=y+1, column=x, sticky="nsew")

