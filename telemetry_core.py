# telemetry_core.py — Shared Module
import time

# Generator: Stream values one at a time
def telemetry_stream(limit, seed):
    for i in range(limit):
        val = (seed * 1.5) + (i * 0.75)
        yield round(val, 2)

# Lambda: Transform & detect anomalies
transform_value = lambda v: round(v * 1.1, 2)
is_abnormal = lambda v, avg: abs(v - avg) > (avg * 0.3)

# Decorator: Log processing timing
def monitor_processing(func):
    def wrapper(*args, **kwargs):
        print(f"📡 [{time.strftime('%H:%M:%S')}] Processing started...")
        result = func(*args, **kwargs)
        print(f"✅ [{time.strftime('%H:%M:%S')}] Processing complete")
        return result
    return wrapper

# Recursion: Analyze condition
analysis_depth = 0
def analyze_condition(value, baseline, depth=1):
    global analysis_depth
    analysis_depth = max(analysis_depth, depth)

    if depth > 5 or value < baseline * 0.5:
        return f"Level {depth}: Critical — Value {value}"
    elif value > baseline * 1.5:
        return analyze_condition(value * 0.8, baseline, depth + 1)
    else:
        return f"Level {depth}: Normal — Value {value}"