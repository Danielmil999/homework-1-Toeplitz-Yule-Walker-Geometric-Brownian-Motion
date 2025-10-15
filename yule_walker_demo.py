# Yule–Walker, step by step (safe version)
# Run from VS Code terminal with:  python3 yule_walker_demo.py

import os
import numpy as np
from scipy.linalg import toeplitz

# 1) implement yule_walker
def yule_walker(y, p):
    # center the data
    y = np.asarray(y, dtype=float)
    T = len(y)
    y = y - y.mean()

    # autocorrelation (biased) and slice needed lags
    ac_full = np.correlate(y, y, mode="full") / T
    mid = len(ac_full) // 2
    # r(0), r(1), ..., r(p)
    r = ac_full[mid: mid + p + 1]  # length p+1

    # build Toeplitz matrix R from r(0..p-1)
    R = toeplitz(r[:-1])           # shape (p, p)
    rhs = r[1:]                    # shape (p,)

    # solve R * phi = rhs
    phi = np.linalg.solve(R, rhs)

    # innovation standard deviation
    sigma = np.sqrt(r[0] - np.dot(phi, rhs))
    return phi, sigma

# 2) try to read vector.csv (AR(2) data). If not found, simulate a clean test series.
def load_or_simulate_series(path="vector.csv", T=500, phi=(0.6, -0.2), sigma=1.0, seed=42):
    if os.path.exists(path):
        y = np.loadtxt(path)
        print(f"Loaded {path} with {len(y)} observations.")
        return y
    else:
        print(f"{path} not found — simulating AR(2) series to test the code.")
        rng = np.random.default_rng(seed)
        e = rng.normal(0.0, sigma, size=T)
        y = np.zeros(T)
        p1, p2 = phi
        for t in range(2, T):
            y[t] = p1 * y[t-1] + p2 * y[t-2] + e[t]
        return y

if __name__ == "__main__":
    # 3) load data (or simulate if missing)
    y = load_or_simulate_series("vector.csv")

    # 4) estimate AR(2) via Yule–Walker
    p = 2
    phi, sigma = yule_walker(y, p)
    print("\nYule–Walker estimates")
    print("---------------------")
    print(f"phi:   {phi}")
    print(f"sigma: {sigma:.4f}")

    # 5) compare to statsmodels AutoReg (if installed)
    try:
        from statsmodels.tsa.ar_model import AutoReg
        model = AutoReg(y, lags=p, old_names=False).fit()
        # params = [const, phi1, phi2] by default
        phi_sm = model.params[1:]  # skip intercept
        sigma_sm = np.sqrt(model.sigma2)
        print("\nstatsmodels AutoReg")
        print("-------------------")
        print(f"phi:   {phi_sm}")
        print(f"sigma: {sigma_sm:.4f}")
    except Exception as e:
        print("\n(statsmodels not installed yet; to compare, run:)")
        print("  python3 -m pip install statsmodels")
