from collections import Counter
import pytest

from dbscan_project.dbscan_alghoritm import My_DBSCAN
from sklearn.datasets import load_iris, make_blobs, make_moons
from sklearn.cluster import DBSCAN as SklearnDBSCAN

def count_clusters_and_points(labels):
    c = Counter(labels)
    noise = c.pop(-1, 0)
    n_clusters = len(c)
    return dict(c), noise, n_clusters

def print_and_compare_results(name, my_labels, sk_labels):
    my_counts, my_noise, my_n_clusters = count_clusters_and_points(my_labels)
    sk_counts, sk_noise, sk_n_clusters = count_clusters_and_points(sk_labels)

    # Output in English
    print(f"\n===== RESULTS FOR DATASET: {name} =====")

    print("\n--- My_DBSCAN ---")
    print(f"Number of clusters: {my_n_clusters}")
    print(f"Number of noise points (-1): {my_noise}")
    for cid in sorted(my_counts):
        print(f"  Cluster {cid}: {my_counts[cid]} points")

    print("\n--- sklearn DBSCAN ---")
    print(f"Number of clusters: {sk_n_clusters}")
    print(f"Number of noise points (-1): {sk_noise}")
    for cid in sorted(sk_counts):
        print(f"  Cluster {cid}: {sk_counts[cid]} points")


def test_iris_display():
    iris = load_iris()
    X_list = iris.data.tolist()
    X_np = iris.data

    eps = 0.7
    min_samples = 5

    my_labels = My_DBSCAN(eps=eps, min_samples=min_samples).fit_predict(X_list)
    sk_labels = SklearnDBSCAN(eps=eps, min_samples=min_samples).fit_predict(X_np)

    print_and_compare_results("IRIS", my_labels, sk_labels)


def test_make_blobs_display():
    X_np, _ = make_blobs(n_samples=400, centers=3, cluster_std=0.5, random_state=42)
    X_list = X_np.tolist()

    eps = 0.8
    min_samples = 5

    my_labels = My_DBSCAN(eps=eps, min_samples=min_samples).fit_predict(X_list)
    sk_labels = SklearnDBSCAN(eps=eps, min_samples=min_samples).fit_predict(X_np)

    print_and_compare_results("MAKE_BLOBS", my_labels, sk_labels)


def test_make_moons_display():
    X_np, _ = make_moons(n_samples=300, noise=0.05, random_state=42)
    X_list = X_np.tolist()

    eps = 0.3
    min_samples = 5

    my_labels = My_DBSCAN(eps=eps, min_samples=min_samples).fit_predict(X_list)
    sk_labels = SklearnDBSCAN(eps=eps, min_samples=min_samples).fit_predict(X_np)

    print_and_compare_results("MAKE_MOONS", my_labels, sk_labels)