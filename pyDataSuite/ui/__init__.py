"""
The UI package is a collection of modules that are used
to create various components of pyDataSuite's user interface.

It also contains, as a submodule, the Azure-tk-theme package, which
is used to customize the look and feel of the UI. It makes the entire
application appear much more modern.
"""

import tkinter as tk
from abc import ABC, abstractmethod
from PIL import ImageTk, Image

class UI_Base( ABC ):
    """
    Base class for UI components.
    """

    def __init__( self, master: tk.Tk, hide_titlebar: bool=False, clear_master: bool=True ):
        self.master = master
        self.master.overrideredirect( hide_titlebar )
        if clear_master:
            self.clear_master()
        self.generate_ui()

    def clear_master( self ):
        """ Clear the master window """
        
        # Clear all children from Tk master
        for child in self.master.winfo_children():
            child.destroy()

    @abstractmethod
    def generate_ui( self ):
        """ Generate the UI contents for this screen """