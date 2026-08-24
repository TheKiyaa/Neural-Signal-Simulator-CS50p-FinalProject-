# Neural Signal Simulator & Analyzer
#### Description:

This project implements a **Neural Signal Simulator & Analyzer** — a command-line tool for generating synthetic neural signals and computing basic statistical and spectral features. It was built as the final project for CS50's Introduction to Programming with Python (CS50P).

## Project Overview

The tool simulates three fundamental types of neural signals commonly used in computational neuroscience and brain-computer interface (BCI) research:

1. **Spike Trains** — Discrete action potential times generated via a homogeneous Poisson process, modeling the firing of a single neuron.
2. **Oscillations** — Continuous sinusoidal signals (e.g., alpha, beta, gamma rhythms) with additive Gaussian noise, representing local field potentials (LFP) or EEG rhythms.
3. **Event-Related Potentials (ERPs)** — Gaussian-shaped transient responses time-locked to a stimulus (e.g., P300 component), with configurable latency, amplitude, and width.

In addition to generation, the tool provides an `analyze_signal` function that computes time-domain statistics (mean, standard deviation) and frequency-domain features (peak frequency via periodogram, SNR estimate in dB).

## Files

### `project.py`
Contains the core implementation with five module-level functions:

- **`generate_spike_train(rate_hz, duration_s, seed)`** — Returns a sorted NumPy array of spike times (seconds) drawn from a Poisson process with the given rate.
- **`generate_oscillation(freq_hz, duration_s, fs, noise_level, seed)`** — Returns a noisy sinusoid sampled at `fs` Hz for `duration_s` seconds.
- **`generate_erp(latency_ms, amplitude, duration_s, fs, noise_level, width_ms, seed)`** — Returns a Gaussian ERP pulse embedded in noise, with peak at `latency_ms` milliseconds.
- **`analyze_signal(sig, fs)`** — Returns a dictionary with keys: `mean`, `std`, `peak_freq_hz`, `snr_estimate_db`. Uses `scipy.signal.periodogram` for spectral analysis.
- **`main()`** — Command-line interface using `argparse` with three modes (`spike`, `osc`, `erp`). Outputs are saved as `.npz` files for further analysis.

All functions are at module level (not nested) and include type hints and docstrings per CS50P requirements.

### `test_project.py`
Four unit tests using `pytest`, one per generation/analysis function:

- **`test_generate_spike_train`** — Verifies output is a sorted 1D array within the time bounds, approximate rate matching, and reproducibility with seeds.
- **`test_generate_oscillation`** — Checks array shape, absence of NaN/Inf, and that the peak frequency matches the target within 1 Hz.
- **`test_generate_erp`** — Validates output shape and that the peak latency/amplitude fall within expected tolerances (±20 ms, ±30%).
- **`test_analyze_signal`** — Tests the full analysis pipeline on a known 10 Hz clean sine wave, confirming dictionary keys, mean ≈ 0, std ≈ 0.7, peak frequency ≈ 10 Hz, and positive SNR.

All tests pass with `pytest test_project.py -v`.

### `requirements.txt`
```
numpy>=1.24.0
scipy>=1.10.0
```
Only two dependencies: NumPy for array operations and random number generation, SciPy for the periodogram spectral estimation.

### `README.md`
This file.

## Design Choices

**Why synthetic signals instead of real data?**
Real neural datasets (EEG, MEG, spikes) require large downloads, specialized formats (.edf, .mat, .nwb), and preprocessing pipelines. For a focused CS50P project, synthetic generation demonstrates the same signal processing concepts (Poisson processes, Fourier analysis, ERP modeling) without external dependencies or data licensing issues. It also provides exact ground truth for testing.

**Why Poisson for spikes?**
The homogeneous Poisson process is the canonical null model for neural spiking. It captures the key statistical property (exponential inter-spike intervals) while remaining simple to implement and reason about.

**Why periodogram for spectral analysis?**
`scipy.signal.periodogram` provides a straightforward, well-tested Welch's method implementation. More advanced methods (multitaper, wavelet) would add complexity without changing the core demonstration.

**Why CLI with `argparse`?**
A command-line interface makes the tool scriptable and reproducible — essential for scientific workflows. The `--seed` parameter ensures exact reproducibility across runs.

**Why `.npz` output?**
NumPy's compressed format preserves array structure and metadata (sampling rate, parameters) without requiring a custom schema. It's the de facto standard for numerical data in Python.

## Usage Examples

```bash
# Generate a 10 Hz spike train for 1 second
python project.py --mode spike --rate 10 --duration 1 --output spikes.npz --seed 42

# Generate a 10 Hz alpha oscillation (2 seconds, 1000 Hz sampling)
python project.py --mode osc --freq 10 --duration 2 --fs 1000 --output alpha.npz --seed 42

# Generate a P300-like ERP at 300 ms latency, 5 μV amplitude
python project.py --mode erp --latency 300 --amplitude 5 --duration 1 --output erp.npz --seed 42
```

## Future Extensions

- Inhomogeneous Poisson processes (rate-modulated spiking)
- Multiple oscillation components (e.g., alpha + gamma coupling)
- ERP components with multiple peaks (N1, P2, P300)
- Time-frequency analysis (wavelets, spectrograms)
- Batch generation for machine learning dataset creation