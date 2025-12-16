.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/dbscan-project.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/dbscan-project
    .. image:: https://readthedocs.org/projects/dbscan-project/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://dbscan-project.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/dbscan-project/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/dbscan-project
    .. image:: https://img.shields.io/pypi/v/dbscan-project.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/dbscan-project/
    .. image:: https://img.shields.io/conda/vn/conda-forge/dbscan-project.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/dbscan-project
    .. image:: https://pepy.tech/badge/dbscan-project/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/dbscan-project
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/dbscan-project

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

==============
dbscan-project
==============


   The project implements the DBSCAN clustering algorithm from scratch in Python as a class called My_DBSCAN. 
The algorithm groups points based on density using the parameters eps and min_samples, and it marks outliers as noise (-1). 
The project also includes pytest tests that compare the custom implementation with sklearn.DBSCAN by checking the number of clusters, 
the number of points in each cluster, and the number of noise points on the Iris, make_blobs, and make_moons datasets. 
In addition, a simple runtime test is included to compare performance.

## Goal of the project
- Implement DBSCAN from scratch in Python
- Compare outputs with scikit-learn DBSCAN
- Provide tests and reproducible project structure (PyScaffold + VirtualEnv + Git)

## Requirements
- Python 3.x
- pytest
- scikit-learn

## Comparison strategy
Direct label comparison is not reliable because cluster IDs can be different.
The project compares:
- number of clusters
- number of noise points
- number of points per cluster
for:
- IRIS
- make_blobs
- make_moons


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
