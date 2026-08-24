import numpy as np
from project import generate_spike_train
from project import generate_oscillation, generate_erp
from project import generate_spike_train, generate_oscillation, generate_erp, analyze_signal

def test_generate_spike_train():
    # تعیین مقادیر ورودی برای تست
    rate = 10.0
    duration = 2.0
    
    # فراخوانی تابع با یک سید (seed) مشخص برای تکرارپذیری
    spikes = generate_spike_train(rate_hz=rate, duration_s=duration, seed=42)
    
    # ۱. بررسی اینکه آیا خروجی حتماً یک آرایه نامپای است؟
    assert isinstance(spikes, np.ndarray)
    
    # ۲. بررسی اینکه آیا زمان‌ها مرتب شده (از کوچک به بزرگ) هستند؟
    assert np.all(np.diff(spikes) >= 0)
    
    # ۳. بررسی اینکه آیا زمان تمام اسپایک‌ها در محدوده مجاز (بین ۰ تا ۲ ثانیه) است؟
    if len(spikes) > 0:
        assert np.min(spikes) >= 0
        assert np.max(spikes) <= duration


def test_generate_oscillation():
    fs = 1000
    duration = 1.0

    sig = generate_oscillation(freq_hz=10.0, duration_s=duration, fs=fs, seed=42)

    # ۱. بررسی اینکه آیا خروجی حتماً آرایه نامپای است؟
    assert isinstance(sig, np.ndarray)
    
    # ۲. بررسی اینکه آیا طول سیگنال دقیقاً برابر با (زمان ضربدر فرکانس نمونه‌برداری) است؟
    assert len(sig) == int(duration * fs)


def test_generate_erp():
    fs = 1000
    duration = 1.0
    
    # فراخوانی تابع با تاخیر ۳۰۰ میلی‌ثانیه و دامنه ۵
    sig = generate_erp(latency_ms=300.0, amplitude=5.0, duration_s=duration, fs=fs, seed=42)
    
    # ۱. بررسی نوع خروجی
    assert isinstance(sig, np.ndarray)
    
    # ۲. بررسی طول سیگنال
    assert len(sig) == int(duration * fs)



def test_analyze_signal():
    fs = 1000
    # تولید یک سیگنال بدون نویز برای تست دقیق‌تر
    sig = generate_oscillation(freq_hz=10.0, duration_s=1.0, fs=fs, noise_level=0.0, seed=42)
    result = analyze_signal(sig, fs)
    
    assert isinstance(result, dict)
    assert "mean" in result
    assert "std" in result
    assert "peak_freq_hz" in result
    assert "snr_estimate_db" in result
    # از اونجایی که سیگنال ۱۰ هرتز ساختیم، انتظار داریم فرکانس غالب هم همون عدد باشه
    assert result["peak_freq_hz"] == 10.0


