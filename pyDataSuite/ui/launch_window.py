"""
launch_window.py is the main entrypoint of pyDataSuite's user interface.
It allows the user to load previous projects, and start new ones.
"""

# System
import tkinter as tk
import tkinter.ttk as ttk

# Package
from . import *
from .create_project import CreateProject

class LaunchWindow( UI_Base ):
    """
    LaunchWindow is the main entrypoint of pyDataSuite's user interface.
    It allows the user to load previous projects, and start new ones.
    """

    def __init__( self, master: tk.Tk ):
        super().__init__( master )
        master.overrideredirect( False )

    def generate_ui(self):
        """ Generate the UI contents for the Launch Window """

        root_frame = ttk.Frame( self.master )
        root_frame.pack( side="top", fill="both", expand=True )

        button = ttk.Button( root_frame, text="Create Project", command=self.create_project )
        button.grid( row=0, column=1, columnspan=2, padx=10, pady=10, sticky="nsew" )

    # UI Actions
    def create_project( self ):
        "Switch to the create project screen"

        CreateProject( self.master )