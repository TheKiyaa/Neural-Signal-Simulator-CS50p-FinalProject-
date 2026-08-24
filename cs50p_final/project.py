import argparse
import numpy as np
from scipy import signal

def generate_spike_train(rate_hz, duration_s, seed=None):
    """
    Generate a homogeneous Poisson spike train.
    """
    if seed is not None:
        np.random.seed(seed)
        
    #۱. محاسبه تعداد اسپایک‌ها با توزیع پواسون
    n_spike = np.random.poisson(rate_hz * duration_s)
    #۲. تولید زمان‌های تصادفی با توزیع یکنواخت برای اسپایک‌ها
    spike_times = np.random.uniform(0 , duration_s, n_spike)
    #۳. مرتب کردن زمان‌ها از کوچک به بزرگ و برگرداندن (return) آن‌ها
    spike_times = np.sort(spike_times)

    return spike_times

def generate_oscillation(freq_hz, duration_s, fs=1000, noise_level=0.1, seed=None):
    if seed is not None:
        np.random.seed(seed)
        
        # مرحله ۱: ساخت آرایه زمان از صفر تا پایان با گام‌های زمانی متناسب با فرکانس نمونه‌برداری
    t = np.arange(0, duration_s, 1/fs)    
    # مرحله ۲: تولید موج سینوسی خالص با استفاده از فرمول ریاضی
    clean_signal = np.sin(2 * np.pi * freq_hz * t)
        
    
    # مرحله ۳: تولید نویز تصادفی به اندازه طول آرایه زمان
    noise = np.random.normal(0, noise_level, len(t))
    
    # مرحله ۴: جمع سیگنال خالص با نویز و بازگرداندن آن
    signal = clean_signal + noise

    return signal


def generate_erp(latency_ms, amplitude, duration_s=1.0, fs=1000, noise_level=0.1, width_ms=50.0, seed=None):
    if seed is not None:
        np.random.seed(seed)
        
    # ۱. ساخت آرایه زمان (مثل تابع قبل، اما در نهایت ضرب در 1000 کن تا تبدیل به میلی‌ثانیه بشه)
    t = np.arange(0, duration_s, 1/fs) * 1000    
    # ۲. پیاده‌سازی فرمول گوسی با استفاده از np.exp
    gaussian = amplitude * np.exp(-((t - latency_ms) ** 2) / (2 * width_ms ** 2))    
    # ۳. تولید نویز تصادفی (دقیقاً مثل تابع قبل)
    noise = np.random.normal(0, noise_level, len(t))    
    # ۴. جمع سیگنال زنگوله‌ای با نویز و بازگرداندن آن
    erp = gaussian + noise

    return erp

def analyze_signal(sig, fs):
    # ۱. محاسبه میانگین و انحراف معیار سیگنال (به float تبدیل کن تا استاندارد باشه)
    # mean_val 
    mean_val = float(np.mean(sig))
    # std_val 
    std_val = float(np.std(sig))
    # ۲. پیدا کردن فرکانس غالب با ابزار periodogram
   
   
    from scipy import signal as sp_signal
    freqs, psd = sp_signal.periodogram(sig, fs=fs)
    peak_freq = float(freqs[np.argmax(psd)])
    
    # ۳. محاسبه توان سیگنال (میانگینِ توان دوم سیگنال) و کف نویز (میانه psd)
    signal_power = np.mean(sig ** 2)
    noise_floor = np.median(psd)
    
    # ۴. محاسبه SNR با فرمول لگاریتمی (از np.log10 استفاده کن)
    if noise_floor == 0:
        snr = float("inf")
    else:
        snr = 10 * np.log10(signal_power/noise_floor)
    
    # ۵. برگرداندن دیکشنری خروجی
    return {
        "mean": mean_val,
        "std": std_val,
        "peak_freq_hz": peak_freq,
        "snr_estimate_db": snr
    }
    
def main():
    parser = argparse.ArgumentParser(
        description="Neural Signal Simulator"
        )
    
    # ۱. آرگومان‌های ضروری و اصلی
    parser.add_argument("--mode", choices=["spike", "osc", "erp"], required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--seed", type=int, default=None)
    
    #۲. اضافه کردن بقیه آرگومان‌ها (مثل --rate برای اسپایک، --freq برای موج و ...)
    parser.add_argument("--rate", type=float, default=10.0)
    parser.add_argument("--duration", type=float, default=1.0)
    parser.add_argument("--freq", type=float, default=10.0)
    parser.add_argument("--fs", type=float, default=1000)
    parser.add_argument("--noise-level", type=float, default=0.1)

    parser.add_argument("--latency", type=float, default=300.0)
    parser.add_argument("--amplitude", type=float, default=1.0)
    parser.add_argument("--width", type=float, default=50.0)
    


    args = parser.parse_args()
    
    # ۳. منطق تصمیم‌گیری بر اساس نوع سیگنال
    if args.mode == "spike":
        #فراخوانی تابع generate_spike_train با آرگومان‌های مناسب
        data = generate_spike_train(
            args.rate,
            args.duration,
            args.seed
        )
        # np.savez(args.output, spike_times=data, rate=args.rate, duration=args.duration)
        np.savez(
            args.output,
            spike_times=data,
            rate=args.rate,
            duration=args.duration
        )
        
    elif args.mode == "osc":
        #فراخوانی تابع generate_oscillation و ذخیره آن
        data = generate_oscillation(
             args.freq,
             args.duration,
             args.fs,
             args.noise_level,
             args.seed
        )

        np.savez(
            args.output,
            signal=data,
            fs=args.fs
        )
        
        
    elif args.mode == "erp":
        #فراخوانی تابع generate_erp و ذخیره آن
        data = generate_erp(
            args.latency,
            args.amplitude,
            args.duration,
            args.fs,
            args.noise_level,
            args.width,
            args.seed
        )

        np.savez(
            args.output,
            signal=data,
            fs=args.fs,
            latency=args.latency,
            amplitude=args.amplitude
        )
        
        
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()