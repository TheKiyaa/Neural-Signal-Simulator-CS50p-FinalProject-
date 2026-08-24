# Neural-Signal-Simulator-CS50p-FinalProject-
CS50P Final Project: A Python CLI tool to generate and analyze synthetic neural signals including spikes, oscillations, and ERPs
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
git clone <https://github.com/TheKiyaa/cs50p-neural-signal-simulator.git>
cd cs50p-neural-signal-simulator
pip install -r requirements.txt

# Generate signals
python project.py --mode spike --rate 10 --duration 1 --output spikes.npz --seed 42
python project.py --mode osc   --freq 10 --duration 2 --fs 1000 --output alpha.npz --seed 42
python project.py --mode erp   --latency 300 --amplitude 5 --duration 1 --output erp.npz --seed 42

# Run tests
pytest test_project.py -v
