Argotrajplot
============

A Python package for plotting Argo float trajectories maps.

Features
--------

- Retrieves and processes Argo float trajectory data
- Plot Argo float trajectories on geographical maps
- Customizable styling and annotations
- Export capabilities for publication-quality figures

Installation
------------

Install via pip:

.. code-block:: bash

    pip install argotrajplot

Quick Start
-----------

.. code-block:: python

    import argotrajplot as atp
    
    # Load trajectory data
    traj = atp.load_index(src='gdac', wmo='4901234', time_range=('2020-01-01', '2021-01-01'))
    
    # Create and display map
    styler = atp.Styler(ocean_color='lightblue', land_color='gray', trajectory_color='red', line_width=1, dpi=100, figsize=(10, 6))
    map_plot = atp.plot_trajectory(traj, projection=ccrs.PlateCarree(),styler=styler)    

Requirements
------------

- Python >= 3.10
- numpy
- xarray
- cartopy
- matplotlib
- shapely


Contributing
------------

Contributions are welcome! Please submit pull requests or open issues on GitHub.

License
-------

MIT License - See LICENSE file for details

Support
-------

For issues and questions, please visit the `GitHub repository <https://github.com/quai20/OneOceanArgo/argotrajplot>`_.