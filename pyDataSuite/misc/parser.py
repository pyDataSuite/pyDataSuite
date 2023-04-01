"""
A simple argument parser for the pyDataSuite user interface.

Doesn't have a lot of options currently, but controlling loglevel could
be useful.
"""

from argparse import ArgumentParser as _ArgumentParser

_parser = _ArgumentParser( 
    prog="pyDataSuite",
    description="""
        A GUI Application for data manipulation, visualization, analysis, 
        and presentation. Compatible with Windows and Linux. Built on
        libraries contained in Anaconda3 Version 4.4.0"""
)

_parser.add_argument(
    "-ll", "--loglevel", default="INFO", help="Select logging verbosity",
    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
)

args = _parser.parse_args()