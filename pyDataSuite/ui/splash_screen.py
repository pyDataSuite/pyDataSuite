"""
loading_screen.py is the first visible part of pyDataSuite's user interface.
It is simply a splash screen to show before the application loads.
"""

# System
import tkinter as tk
import tkinter.ttk as ttk

# Package
from . import UI_Base

class SplashScreen( UI_Base ):
    """
    SplashScreen is the main entrypoint of pyDataSuite's user interface.
    It allows the user to load previous projects, and start new ones.
    """

    def __init__( self, master: tk.Tk ):
        super().__init__( master )
        
        # Remove window title bar
        master.overrideredirect( True )

    def generate_ui(self):
        """ Generate the UI contents for the Launch Window """
        pass