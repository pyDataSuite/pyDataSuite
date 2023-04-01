"""
This file turns project resources into importable objects.
"""

# System
from PIL import Image
from pathlib import Path

# Package
from pyDataSuite.misc import logs

# Constants
_path = Path( __file__ ).parent / 'images'
_log  = logs.logger()

# Project Assets
if ( _path / 'graph.png' ).exists():
    icon_project_default = Image.open( _path / 'graph.png' )
    icon_project_default = icon_project_default.resize( ( 100, 100 ), Image.ANTIALIAS )
else:
    _log.error( "Image resource not found: graph.png" )
    icon_project_default = Image.new( "RGB", ( 100, 100 ), ( 255, 0, 0 ) )