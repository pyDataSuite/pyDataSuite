"""
project_page is the main interface for managing pyDataSuite projects.

It allows the user to manage the data in the project, create visualizations,
and create presentations. Really this interface is just a compilation of the
smaller component interfaces.
"""

# System
import tkinter as tk
import tkinter.ttk as ttk

# Package
from pyDataSuite.misc.data import populate_dataset_tree
from . import *

class DataPage( ttk.Frame ):
    """
    Datapage is where datasets can be imported, parametrically modified,
    and prepared for whatever purpose they may be used for
    """

    def __init__(self, master: tk.Tk ) -> None:
        super().__init__( master )

        # Create treeview
        self.treeview = ttk.Treeview( self, selectmode='none' )
        self.treeview.grid( row=0, column=0, padx=10, pady=10, sticky="nsew" )
        self.treeview.bind( "<Button-1>", self.treeselect )
        self.treeselection = []

        # Set up treeview
        self.treeview.heading( "#0", text="Datum", anchor="center" )
        populate_dataset_tree( self.treeview )

        # Set up grid
        self.grid_columnconfigure( 0, weight=1 )
        self.grid_rowconfigure( 0, weight=1 )

    def treeselect( self, event ):
        """
        Handle a click on the treeview.
        """

        # Get the selected item
        item_name = self.treeview.identify_row( event.y )
        if item_name:
            tags = self.treeview.item( item_name, 'tags' )

            # If dataset, toggle selecting it
            if tags and ( tags[ 0 ] == "dataset" ):
                if item_name in self.treeselection:
                    self.treeselection.remove( item_name )
                else:
                    self.treeselection.append( item_name )
                self.treeview.selection_set( self.treeselection )


            # If group, toggle expanding or closing it
            elif tags and ( tags[ 0 ] == "group" ):
                is_open = self.treeview.item( item_name, "open")
                self.treeview.item( item_name, open=not is_open )
                    

class ProjectPage( UI_Base ):
    """
    ProjectPage is the main interface for managing pyDataSuite projects.
    It allows the user to manage the data in the project, create visualizations,
    and create presentations. Really this interface is just a compilation of the
    smaller component interfaces.
    """
    
    def __init__( self, master: tk.Tk ):
        super().__init__( master )
        
        # Maximize window
        master.state( 'zoomed' )
        
    def generate_ui(self):
        """ Generate the UI contents for the Launch Window """
        
        root_frame = ttk.Frame( self.master )
        root_frame.pack( side="top", fill="both", expand=True )

        #
        # Start ribbon using notebook
        #
        self.ribbon = ttk.Notebook( root_frame, height=70 )
        self.ribbon.grid( row=0, column=0, columnspan=2, sticky="nsew" )

        # Data tab
        self.data_tab = ttk.Frame( self.ribbon )
        self.ribbon.add( self.data_tab, text="Data" )
        ttk.Label( self.data_tab, text="Data" ).grid( row=0, column=0, padx=10, pady=10, sticky="nsew" )

        # Visualization tab
        self.visualization_tab = ttk.Frame( self.ribbon )
        self.ribbon.add( self.visualization_tab, text="Visualization" )
        ttk.Label( self.visualization_tab, text="Visualization" ).grid( row=0, column=0, padx=10, pady=10, sticky="nsew" )

        # Presentation tab
        self.presentation_tab = ttk.Frame( self.ribbon )
        self.ribbon.add( self.presentation_tab, text="Presentation" )
        ttk.Label( self.presentation_tab, text="Presentation" ).grid( row=0, column=0, padx=10, pady=10, sticky="nsew" )

        #
        # Set up data page
        #
        self.data_page = DataPage( root_frame )
        self.data_page.grid( row=1, column=0, sticky="nsew" )

        # Set up grid layout
        root_frame.grid_columnconfigure( 0, weight=1 )
        root_frame.grid_columnconfigure( 1, weight=1 )
        root_frame.grid_rowconfigure( 1, weight=1 )