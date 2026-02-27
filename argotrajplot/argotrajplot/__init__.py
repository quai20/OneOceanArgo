
"""
Argotrajplot: A Python package for plotting Argo float trajectories maps.
"""

__version__ = "0.1.0"
__author__ = "Kevin Balem"
__email__ = "kevin.balem@ifremer.fr"

from .atp_core import load_index, plot_trajectory
from .atp_styler import Styler

# Import main functions and classes
try:
    pass
except ImportError:
    pass

__all__ = [
    "load_index",
    "plot_trajectory",
    "Styler",
]
