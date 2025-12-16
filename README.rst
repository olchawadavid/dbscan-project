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

Requirements
• Python 3.x
• pytest (for running tests)
• scikit-learn (for dataset generation and comparison)

2. Algorithm description
DBSCAN finds clusters as connected dense regions and labels isolated points as noise.
It is useful for irregular cluster shapes and for outlier detection.

Parameters
• eps: neighborhood radius. Two points are neighbors if their distance is less than or equal to eps.
• min_samples: minimum number of neighbors required to treat a point as dense (a core point).

Point types
• Core point: has at least min_samples neighbors within eps.
• Border point: not dense enough to be core, but reachable from a core point.
• Noise point: not reachable from any cluster; labeled as -1.

Distance metric
This project uses Euclidean distance:
d(p, q) = sqrt( sum_i (p_i - q_i)^2 )

3. User manual
Class: My_DBSCAN
File: src/dbscan_project/dbscan_alghoritm.py

Constructor
My_DBSCAN(eps=0.5, min_samples=5)

Parameters:
• eps (float > 0): neighborhood radius
• min_samples (int > 0): minimum neighbors for a core point

Input format
X should be a list of points, for example: [[x1, y1], [x2, y2], ...].
All points must have the same number of features.

Methods
• fit(X): runs clustering and stores results in self.labels and self.n_clusters; returns self.
• fit_predict(X): calls fit(X) and returns self.labels.

Output labels
• -1 means noise
• 1, 2, 3, ... are cluster IDs
• 0 is used only internally for unassigned points
.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
