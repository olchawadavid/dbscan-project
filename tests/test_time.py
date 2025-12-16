# tests/test_time_minimal.py
from time import perf_counter
import pytest

from dbscan_project.dbscan_alghoritm import My_DBSCAN
from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import DBSCAN as SklearnDBSCAN


def test_time_comparison_minimal():
    repeats = 3

    test_scenarios = [
        ("make_blobs", 200, 0.6, 5),
        ("make_blobs", 2000, 0.6, 5),
        ("make_blobs", 4000, 0.6, 5),

        ("make_moons", 200, 0.25, 5),
        ("make_moons", 2000, 0.25, 5),
        ("make_moons", 4000, 0.25, 5),
    ]

    print("\n\n========= TIME TEST: My_DBSCAN vs sklearn.DBSCAN ========")

    for name, n, eps, min_samples in test_scenarios:

        if name == "make_blobs":
            X_np, _ = make_blobs(n_samples=n, centers=4, cluster_std=0.6, random_state=42)
        elif name == "make_moons":
            X_np, _ = make_moons(n_samples=n, noise=0.06, random_state=42)

        X_list = X_np.tolist()

        my_total = 0.0
        for _ in range(repeats):
            model = My_DBSCAN(eps=eps, min_samples=min_samples)
            t0 = perf_counter()
            model.fit_predict(X_list)
            t1 = perf_counter()
            my_total += (t1 - t0)
        my_time = my_total / repeats

        sk_total = 0.0
        for _ in range(repeats):
            model = SklearnDBSCAN(eps=eps, min_samples=min_samples)
            t0 = perf_counter()
            model.fit_predict(X_np)
            t1 = perf_counter()
            sk_total += (t1 - t0)
        sk_time = sk_total / repeats

        ratio = my_time / sk_time if sk_time > 0 else float("inf")

        print(f"\n[{name}] n={n}")
        print(f"My_DBSCAN: {my_time:.4f} s")
        print(f"sklearn  : {sk_time:.4f} s")
        print(f"ratio(my/sk): {ratio:.2f}x")

    assert True