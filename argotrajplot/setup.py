from setuptools import setup, find_packages

setup(
    name="argotrajplot",
    version="0.1.0",
    description="A simple package for optimized Argo trajectory plotting",
    author="Kevin Balem",
    author_email="kevin.balem@ifremer.fr",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        'xarray',
        'numpy',
        'matplotlib',
        'cartopy',
        'shapely',
        'shapelysmooth'
    ]
)
