"""
create_project.py is a form UI that allows the user to create a new project.
"""

# System
import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmsg
import tkinter.ttk as ttk
from PIL import ImageTk
from h5py import File
from pathlib import Path

# Package
from . import *
from .project_page import ProjectPage
from pyDataSuite.resources.images import icon_project_default
from pyDataSuite.misc.state import state

class CreateProject( UI_Base ):
    """
    CreateProject is a form UI that allows the user to create a new project.
    """

    def generate_ui(self):
        """ Generate the UI contents for the Launch Window """

        root_frame = ttk.Frame( self.master )
        root_frame.pack( side="top", fill="both", expand=True )

        # Header for this screen
        ttk.Label( 
            root_frame, 
            text="Create New Project", 
            anchor='center', 
            font=( "Arial", 20 ) 
        ).grid( 
            row=1, column=1, columnspan=2, padx=10, pady=10, sticky="nsew" 
        )

        # Image input element
        img = ImageTk.PhotoImage( icon_project_default )
        l = ttk.Button( root_frame, image=img )
        l.image = img
        l.grid( row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nsew" )

        # Labels for inputs
        ttk.Label( root_frame, text="Project Name" ).grid( row=3, column=1, padx=10, pady=10, sticky="nsew" )
        ttk.Label( root_frame, text="Project Description" ).grid( row=4, column=1, padx=10, pady=10, sticky="nsew" )

        # Inputs
        self.project_name = ttk.Entry( root_frame )
        self.project_name.grid( row=3, column=2, padx=10, pady=10, sticky="nsew" )
        self.project_description = ttk.Entry( root_frame )
        self.project_description.grid( row=4, column=2, padx=10, pady=10, sticky="nsew" )

        # Button to create project
        ttk.Button( root_frame, text="Begin", command=self.create_project ).grid(
            row=5, column=1, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # Set up grid layout for the screen
        root_frame.grid_columnconfigure( 0, weight=1 )
        root_frame.grid_columnconfigure( 2, weight=1 )
        root_frame.grid_columnconfigure( 3, weight=1 )
        root_frame.grid_rowconfigure( 0, weight=1 )
        root_frame.grid_rowconfigure( 6, weight=1 )

    def create_project( self ):
        """ 
        Generates a file that will hold the new project, and 
        switches to the project management screen when the project is created.
        """

        # Get the project name
        project_name = self.project_name.get()

        # Get the project description
        project_description = self.project_description.get()

        # Validate user inputs
        if not project_name:
            tkmsg.showerror( "Error", "Project name cannot be empty" )
            return
        if not project_description:
            tkmsg.showerror( "Error", "Project description cannot be empty" )
            return

        # Prompt for the save location
        requested_file = tkfd.asksaveasfile(
            parent=self.master,
            initialdir=Path.home(),
            title="Select Save Location",
            defaultextension=".pds",
            filetypes=[ ( "pyDataSuite Files", "*.pds" ), ( "All Files", "*.*" ) ]
        )

        # Stop if the user cancelled the save
        if not requested_file:
            return
        save_location = Path( requested_file.name )
        
        # Create the project
        state.File = File( save_location, "w" )
        state.File.attrs["project_name"] = project_name
        state.File.attrs["project_description"] = project_description
        state.File.create_group( "Data" )
        state.File.create_group( "Visualizations" )
        state.File.create_group( "Presentation" )
        
        # For testing purposes only
        state.File["Data"].create_dataset( "mydata", data=[1, 2, 3, 4, 5, 6, 7] )

        # state.File.close()

        # Switch to the project management screen
        ProjectPage( self.master )