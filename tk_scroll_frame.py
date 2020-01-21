from tkinter import *
from tkinter import ttk


class VerticalScrolledFrame(ttk.Frame):
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")  

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)   

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>") 

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=self.canvas.yview)
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        self.interior = interior = ttk.Frame(self.canvas)
        interior_id = self.canvas.create_window(0, 0, window=interior, anchor=NW)

        def _configure_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            self.canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.itemconfigure(interior_id, width=self.canvas.winfo_width())

        self.canvas.bind('<Configure>', _configure_canvas)
        
        self.canvas.bind('<Enter>', self._bound_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbound_to_mousewheel)
