**GitHub Repo Description (برای کپی در بخش About/Description ریپو):**

```
Neural Signal Simulator & Analyzer — CS50P Final Project. Generate synthetic neural signals (Poisson spike trains, noisy oscillations, Gaussian ERPs) and compute spectral statistics via CLI. Pure Python (NumPy, SciPy) with full test coverage.
```

---

**GitHub Topics (برای کپی در بخش Topics ریپو - با کاما جدا کن):**

```
cs50p, neural-signals, computational-neuroscience, bci, eeg-simulation, spike-trains, erp, python, scipy, numpy
```

---

**README.md (نسخه کامل مصقول برای جایگزینی فایل فعلی - کپی کن و جایگزین کن):**

```markdown
# Neural Signal Simulator & Analyzer

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CS50P](https://img.shields.io/badge/CS50P-Final%20Project-orange.svg)](https://cs50.harvard.edu/python/)

A command-line tool for **generating synthetic neural signals** and **computing statistical/spectral features** — built as the final project for [CS50's Introduction to Programming with Python (CS50P)](https://cs50.harvard.edu/python/).

#### Video Demo: [Add your YouTube link here]

---

## Features

| Signal Type | Description | Parameters |
|-------------|-------------|------------|
| **Spike Trains** | Homogeneous Poisson process modeling single-neuron firing | `rate_hz`, `duration_s` |
| **Oscillations** | Noisy sinusoids (EEG/LFP rhythms: alpha, beta, gamma) | `freq_hz`, `fs`, `noise_level` |
| **ERPs** | Gaussian event-related potentials (P300-like) | `latency_ms`, `amplitude`, `width_ms` |
| **Analysis** | Time-domain + spectral stats (peak freq, SNR via periodogram) | `sig`, `fs` |

---

## Quick Start

```bash
# Clone & install
git clone https://github.com/TheKiyaa/cs50p-neural-signal-simulator.git
cd cs50p-neural-signal-simulator
pip install -r requirements.txt

# Generate signals
python project.py --mode spike --rate 10 --duration 1 --output spikes.npz --seed 42
python project.py --mode osc   --freq 10 --duration 2 --fs 1000 --output alpha.npz --seed 42
python project.py --mode erp   --latency 300 --amplitude 5 --duration 1 --output erp.npz --seed 42

# Run tests
pytest test_project.py -v
```

---

## Project Structure

```
.
├── project.py           # Core implementation (5 functions + CLI)
├── test_project.py      # 4 pytest unit tests (all passing)
├── requirements.txt     # numpy, scipy
├── .gitignore           # Excludes __pycache__, *.npz, .pytest_cache
└── README.md            # This file
```

### Core Functions (`project.py`)

| Function | Returns | Description |
|----------|---------|-------------|
| `generate_spike_train(rate_hz, duration_s, seed)` | `np.ndarray` | Sorted spike times (seconds) |
| `generate_oscillation(freq_hz, duration_s, fs, noise_level, seed)` | `np.ndarray` | Noisy sinusoid samples |
| `generate_erp(latency_ms, amplitude, duration_s, fs, noise_level, width_ms, seed)` | `np.ndarray` | Gaussian ERP pulse + noise |
| `analyze_signal(sig, fs)` | `dict` | `mean`, `std`, `peak_freq_hz`, `snr_estimate_db` |
| `main()` | — | `argparse` CLI entry point |

All functions are **module-level** with type hints and docstrings (CS50P compliant).

---

## Design Decisions

- **Synthetic data** — No external dependencies, exact ground truth for testing
- **Poisson spikes** — Canonical null model for neural spiking statistics
- **Periodogram (Welch)** — Standard, well-tested spectral estimation via SciPy
- **CLI + seeds** — Reproducible, scriptable scientific workflows
- **`.npz` output** — Standard NumPy format preserving arrays + metadata

---

## Requirements

```
numpy>=1.24.0
scipy>=1.10.0
```

---

## Testing

```bash
pytest test_project.py -v
# 4 tests: spike train, oscillation, ERP, signal analysis → all PASS
```

---

## Future Work

- Inhomogeneous Poisson processes (rate-modulated spiking)
- Multi-component oscillations (cross-frequency coupling)
- Multi-peak ERPs (N1, P2, P300)
- Time-frequency analysis (wavelets, spectrograms)
- Batch generation for ML dataset creation

---

## License

MIT License — free to use, modify, and distribute.

---

## Author

**Mohammad Kia Ghasemi**
- GitHub: [@TheKiyaa](https://github.com/TheKiyaa)
- LinkedIn: [mohammad-kia-ghasemi](https://www.linkedin.com/in/mohammad-kia-ghasemi)
- CS50P Certificate: 2026
```

---

**می‌خوای این README جایگزین کنم در فایل؟** بگو `replace کن` تا بنویسم.
