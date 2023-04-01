"""
A simple module that contains many of the data handling functions required
throughout the pyDataSuite user interface.
"""

# System
from h5py import File, Group, Dataset
import tkinter.ttk as ttk

# Package
from .state import state

def populate_dataset_tree( treeview: ttk.Treeview, root=True, starting_id=-1, fkey="" ):
    """
    Populate the treeview with the datasets in the current project.
    """

    print( f"populate_dataset_tree( { treeview }, { root }, { starting_id } )" )
    
    # Get the data dataset
    if fkey != "":
        data = state.File[ fkey ]
    else:
        data = state.File

    keys = sorted( data.keys() )

    # For each child, add to tree
    for child in keys:
        # starting_id += 1
        new_id = treeview.insert( parent="" if root else starting_id-1, iid=starting_id, index='end', text=child, values=( child, ) )
        print( f"Inserted '{ child }' at { starting_id }" )

        if isinstance( data[ child ], Group ):
            starting_id += populate_dataset_tree( treeview, root=False, starting_id=starting_id, fkey=child )

    return starting_id