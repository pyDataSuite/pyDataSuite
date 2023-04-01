"""
A simple module that contains many of the data handling functions required
throughout the pyDataSuite user interface.
"""

# System
from h5py import File, Group, Dataset
import tkinter.ttk as ttk

# Package
from .state import state

def populate_dataset_tree( treeview: ttk.Treeview, parent="", fkey="" ):
    """
    Populate a treeview with the datasets in the current project.
    """

    # print( f"populate_dataset_tree( { treeview }, { root }, { starting_id } )" )
    
    # Get the data dataset
    if fkey != "":
        data = state.File[ fkey ]
    else:
        data = state.File

    keys = sorted( data.keys() )

    # For each child, add to tree
    for child in keys:

        if isinstance( data[ child ], Group ):
            new_element = treeview.insert( parent=parent, index='end', text=child, values=( child, ), tags="group" )
            populate_dataset_tree( treeview, parent=new_element, fkey=fkey+"/"+child )
        else:
            treeview.insert( parent=parent, index='end', text=child, values=( child, ), tags="dataset" )
