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

**DBSCAN  in Python** + tests comparing results with ``sklearn.DBSCAN``.
The implementation clusters points based on density (``eps`` and ``min_samples``) and marks outliers as noise (label ``-1``).

Key features
============

* Custom DBSCAN class: ``My_DBSCAN``
* Tests on datasets: Iris, ``make_blobs``, ``make_moons``
* Comparison with scikit-learn:
  * number of clusters
  * number of points per cluster
  * number of noise points
* Simple runtime comparison (custom vs sklearn)

Requirements
============

* Python 3.x
* pytest (tests)
* scikit-learn (datasets + reference DBSCAN)

Usage
=====

Class: ``My_DBSCAN``
File: ``src/dbscan_project/dbscan_alghoritm.py``

Algorithm description
=====================

DBSCAN finds clusters as connected dense regions and labels isolated points as noise.
It works well for irregular cluster shapes and outlier detection.

Parameters
----------

* ``eps``: neighborhood radius (two points are neighbors if distance <= eps)
* ``min_samples``: minimum number of neighbors to treat a point as a core point

Point types
-----------

* **Core point**: has at least ``min_samples`` neighbors within ``eps``
* **Border point**: not dense enough to be core, but reachable from a core point
* **Noise point**: not reachable from any cluster; labeled as ``-1``

Distance metric
---------------

Euclidean distance:

.. code-block:: text

   d(p, q) = sqrt( sum_i (p_i - q_i)^2 )


Results / Conclusion
====================

The custom DBSCAN implementation produces the same clustering results as scikit-learn on the tested datasets.
Scikit-learn is faster because it is highly optimized, while the custom version is simpler and easier to understand.

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
