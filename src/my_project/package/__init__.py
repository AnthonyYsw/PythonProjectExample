__version__ = "1.0.0"
__author__ = "Anthony"
__email__ = "anthony.yang.22@ucl.ac.uk"

from . import recursion
from . import basic_math

from .recursion import *
from .basic_math import *

__all__ = ["__version__", "__author__", "__email__"]
__all__.extend(["recursion", "basic_math"])
