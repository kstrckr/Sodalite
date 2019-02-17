import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class Raster_Tab(ttk.Frame):
    def __init__(self, parent):
        # ttk.Frame.__init__(self, parent, *args, **kwargs)
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.raster_canvas = tk.Canvas(self, width=475, height=206)

        self.raster_canvas.grid(column=0, row=0, padx=10, pady=10)

        self.open_button = ttk.Button(self, text="  Select Image  ", command=self.get_image_path)
        self.open_button.grid(column=0, row=1, ipady=15, padx=30, ipadx=15, pady=30, sticky=(tk.N))

    def get_image_path(self):
        filename = fd.askopenfile()
        print(filename.name)
        self.imgobj = tk.PhotoImage(file=filename.name)
        self.raster_canvas.create_image(0, 0, image=self.imgobj, anchor=tk.NW)