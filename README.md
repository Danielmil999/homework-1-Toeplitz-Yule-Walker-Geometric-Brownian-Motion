# Homework 1 — Toeplitz Matrix, Yule–Walker, and Geometric Brownian Motion

This repository contains my solutions to Homework 1. It includes **Python** code for Toeplitz matrices and Yule–Walker estimation, and **R** code for simulating a Geometric Brownian Motion (GBM) and estimating a ruin probability. The repo is organized to be reproducible and easy for instructors to run.

---

## ✅ Assignment checklist (how this repo meets requirements)

- **Clear commit messages** — used throughout (e.g., “Add Toeplitz manual implementation”, “Fix GBM loop indexing”).
- **One issue with TODO list** — created in the Issues tab.
- **One pull request + merge** — created from `dev` branch into `main` and merged.
- **README.md** — this file (overview, file purposes, run instructions).
- **Meaningful file names** — see structure below.
- **.gitignore** — excludes temporary/system files.
- **All code runs start-to-finish** — instructions below reproduce results.
- **Code commented, unused code removed** — done in both Python and R.
- **Rendered Quarto outputs (HTML/PDF)** — provided/ reproducible via instructions.
- **Time spent per exercise** — listed at the end.

---

## 📦 Repository structure (what each file/folder means)

.
├─ README.md # You are here: overview + how to run
├─ .gitignore # Keeps repo clean (ignores caches, temp files)
├─ requirements.txt # Python dependencies for this project
│
├─ toeplitz_homework.py # Python: manual Toeplitz + SciPy comparison + timing
├─ toeplitz_yulewalker.qmd # Quarto (Python): Toeplitz + Yule–Walker (narrative)
│
├─ vector.csv # Input data for AR(2) Yule–Walker estimation
├─ Homework1_geom_Brownian_motion.qmd # Quarto (R): GBM simulation + ruin probability + plots

yaml
Copier le code

**What to look at first**
- Quick demo: run `toeplitz_homework.py` (Python).
- Full writeup + results: render `toeplitz_yulewalker.qmd` (Python Quarto) and `Homework1_geom_Brownian_motion.qmd` (R Quarto).

---

## 🧰 Setup

### 1) Install Quarto (for rendering `.qmd`)
- Download: https://quarto.org/docs/get-started/
- Verify installation:
  ```bash
  quarto --version
2) Python (3.12+ recommended)
Install dependencies (from the repo root):

bash
Copier le code
python3 -m pip install -r requirements.txt
If pip is not found:

bash
Copier le code
python3 -m ensurepip --upgrade
python3 -m pip install -r requirements.txt
3) R (for the GBM part)
In R or RStudio:

r
Copier le code
install.packages("ggplot2")
If you render Quarto from the terminal, make sure R is installed and on your PATH.

▶️ How to run everything (step-by-step)
A) Python script: Toeplitz + timings
From the repo folder:

bash
Copier le code
python3 toeplitz_homework.py
Outputs:

Prints custom Toeplitz vs SciPy Toeplitz

Prints timing comparison via timeit

B) Python Quarto: Toeplitz + Yule–Walker (narrative)
Render to HTML:

bash
Copier le code
quarto render toeplitz_yulewalker.qmd --to html
(Optionally, --to pdf if LaTeX is installed.)

What it does:

Validates inputs for toeplitz_matrix(dim, seq, verbose=...)

Compares with scipy.linalg.toeplitz

Benchmarks both

Implements yule_walker(y, p) with np.linalg.solve and compares to statsmodels.AutoReg

C) R Quarto: GBM ruin probability
Render to HTML:

bash
Copier le code
quarto render Homework1_geom_Brownian_motion.qmd --to html
What it does:

Simulates N GBM paths via Euler–Maruyama

Estimates empirical ruin probability for threshold u

Plots 10 random trajectories and overlays u

If you intentionally keep some error demonstrations:
Add this to the YAML of your .qmd to continue rendering on errors:

yaml
Copier le code
execute:
  error: true
🧪 Reproducibility notes
Randomness: Both Python and R examples set seeds where relevant (np.random.seed / set.seed) to make results reproducible.

Input file: vector.csv is used by the Yule–Walker section; keep it in the repo root.

Performance prints: toeplitz_matrix(..., verbose=False) is used in benchmarks to suppress messages.

🧩 Theory pointers (brief)
Toeplitz minimum dimension vs sequence length:
For the manual construction using a single sequence that fills all needed diagonals, we require
dim ≤ len(seq)
so that every T[i, j] = seq[dim - 1 + i - j] is defined for all 0 ≤ i, j < dim.

Yule–Walker:
Constructs a Toeplitz autocorrelation matrix R from r(k) and solves R Φ = r for AR(p) parameters Φ, with innovation std σ = sqrt(γ(0) − Φᵀ r).

🧹 Clean repo policy
.gitignore excludes __pycache__/, *.pyc, .Rhistory, Quarto cache dirs (*_files/), and system files (e.g., .DS_Store).

Only relevant code, data (vector.csv), and rendered outputs are committed.

All issues are closed and auxiliary branches deleted before submission.

⏱ Time spent (approx.)
Exercise 1 (Toeplitz + Yule–Walker): hh:mm

Exercise 2 (GBM ruin probability in R): hh:mm

Documentation & cleanup: hh:mm

(Replace with your actual times.)

🧑‍💻 Environment (for graders)
macOS / Python 3.12+ / R 4.3+ / Quarto 1.5+

Python libs: numpy, scipy, statsmodels

R libs: ggplot2

📝 Notes for the graders
The PR from dev → main documents the change history.

The issue titled “TODO: finalize benchmarks & README” tracks the checklist and is closed on completion.