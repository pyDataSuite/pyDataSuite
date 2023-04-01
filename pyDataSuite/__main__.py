import tkinter as tk
from pyDataSuite.async_tk import async_tk
from pathlib import Path

root = tk.Tk()

# Load theme
theme_path = Path( __file__ ).parent / 'ui' / 'Azure-ttk-theme' / 'azure.tcl'
root.tk.call( "source", str( theme_path ) )
root.tk.call( "set_theme", "light" )

# Make root 600 by 400 and place it in the middle of the screen
root.geometry( "600x400" )
root.update_idletasks()
root.minsize( root.winfo_width(), root.winfo_height() )
x_cordinate = int( ( root.winfo_screenwidth() / 2 ) - ( root.winfo_width() / 2 ) )
y_cordinate = int( ( root.winfo_screenheight() / 2 ) - ( root.winfo_height() / 2 ) )
root.geometry( "+{}+{}".format( x_cordinate, y_cordinate - 20 ) )

# Set up the initial screen
from pyDataSuite.ui.launch_window import LaunchWindow
LaunchWindow( root )

# Begin the application
async_tk.asyncloop( root )