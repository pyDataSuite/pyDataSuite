# System
import logging as _logging
import inspect as _inspect
import sys as _sys
from pathlib import Path as _Path

# Package
from pyDataSuite import args

_logger = _logging.getLogger( __name__ )

_logging.basicConfig( 
    level=args.loglevel,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S' 
)

def logger( ):
    # Get absolute path of the calling file
    logger_name = _Path( _inspect.getsourcefile( _sys._getframe( 1 ) ) )

    # Truncate path so it starts with 'pyDataSuite/'
    logger_name = logger_name.relative_to( _Path( __file__ ).parents[ 2 ] )
    
    return _logging.getLogger( str( logger_name ) )