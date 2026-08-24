# 🧠 Neural Signal Simulator & Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=white)
![CS50P](https://img.shields.io/badge/CS50P-Harvard-red?style=for-the-badge)

**CS50P Final Project** — A pure Python command-line tool designed to generate and analyze synthetic neural signals, including spikes, oscillations, and Event-Related Potentials (ERPs).

---

## ✨ Features

- **Spike Trains**: Generate homogeneous Poisson spike processes.
- **Oscillations**: Create sinusoidal brain waves with controllable noise levels.
- **ERPs**: Simulate Event-Related Potentials (Gaussian pulses) with additive noise.
- **Signal Analysis**: Extract time-domain statistics, spectral peak frequencies, and estimate Signal-to-Noise Ratio (SNR).
- **CLI & API**: Use it directly from your terminal or import it as a Python module. Outputs are saved as `.npz` files.

## 🚀 Installation

Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/YourUsername/Neural-Signal-Simulator.git](https://github.com/YourUsername/Neural-Signal-Simulator.git)
cd Neural-Signal-Simulator
pip install -r requirements.txt
```

## 💻 Command-Line Usage

Generate a spike train (10 Hz, 1 second):
```bash
python project.py --mode spike --rate 10 --duration 1 --output spikes.npz --seed 42
```

Generate an oscillation (10 Hz alpha wave, 2 seconds, 1000 Hz sampling):
```bash
python project.py --mode osc --freq 10 --duration 2 --fs 1000 --output alpha.npz --seed 42
```

Generate an ERP (P300-like at 300ms, 5μV amplitude):
```bash
python project.py --mode erp --latency 300 --amplitude 5 --duration 1 --output erp.npz --seed 42
```

## 🧩 Python API

You can also use the simulator directly in your Python scripts:

```python
from project import generate_spike_train, generate_oscillation, generate_erp, analyze_signal

# Generate an oscillation signal
signal = generate_oscillation(freq_hz=10, duration_s=1.0, fs=1000, noise_level=0.1, seed=42)

# Analyze the generated signal
stats = analyze_signal(signal, fs=1000)
print(stats)
# Output: {'mean': ..., 'std': ..., 'peak_freq_hz': 10.0, 'snr_estimate_db': ...}
```

## 🧪 Testing

This project includes a comprehensive test suite using `pytest`. To run the tests:

```bash
pytest test_project.py -v
```

## 📁 Project Structure

| File | Description |
|------|-------------|
| `project.py` | Main implementation containing the 5 core functions and CLI logic. |
| `test_project.py` | Unit tests for all signal generation and analysis functions. |
| `requirements.txt` | Project dependencies (`numpy`, `scipy`). |
| `README.md` | This documentation file. |

---
*This project was created as the Final Project for Harvard's CS50 Introduction to Programming with Python.*
