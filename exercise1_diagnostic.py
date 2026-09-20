# EXERCISE 1: Equipment Diagnostic System

# ==========================================
# STUDENT-SPECIFIC INPUTS — EDIT HERE
# ==========================================
LAST_NAME = "VIANA"
SEED_NUM = 3
FAVORITE_ARTIST = "Apo Hiking Society"

# ==========================================
# 1. Generate Student-Specific Readings
# ==========================================
def generate_readings():
    base = len(LAST_NAME) + SEED_NUM
    readings = [
        base * 1.2,
        base * 1.5,
        base * 0.9,
        len(FAVORITE_ARTIST) + SEED_NUM,
        -2.5,          # Invalid: negative
        base * 1.1,
        None,          # Invalid: null
        base * 1.8
    ]
    return readings

# ==========================================
# 2. Validation Function
# ==========================================
def validate_reading(value):
    if value is None:
        return False, "NULL_VALUE"
    if not isinstance(value, (int, float)):
        return False, "INVALID_TYPE"
    if value < 0:
        return False, "NEGATIVE_VALUE"
    if value > 50:
        return False, "OUT_OF_RANGE"
    return True, "VALID"

# ==========================================
# 3. Calculation Function
# ==========================================
def calculate_average(valid_readings):
    if not valid_readings:
        return 0
    return sum(valid_readings) / len(valid_readings)

# ==========================================
# 4. Classification Function
# ==========================================
def classify_equipment(avg):
    if avg >= 15:
        return "EXCELLENT"
    elif avg >= 10:
        return "NORMAL"
    elif avg >= 5:
        return "MONITOR"
    else:
        return "CRITICAL"

# ==========================================
# 5. Decorator — Execution Logging
# ==========================================
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"▶ Running: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✓ Completed: {func.__name__}")
        return result
    return wrapper

# ==========================================
# MAIN PROGRAM
# ==========================================
@log_execution
def main():
    print("=" * 55)
    print("EQUIPMENT DIAGNOSTIC SYSTEM")
    print(f"Operator: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
    print("=" * 55)

    raw_data = generate_readings()
    print("\n[Generated Equipment Readings]")
    print(f"Raw Data: {raw_data}")

    valid_readings = []
    invalid_entries = []
    print("\n[Validation Results]")
    for idx, val in enumerate(raw_data, 1):
        status, note = validate_reading(val)
        print(f"  Reading {idx}: {val} → {note}")
        if status:
            valid_readings.append(val)
        else:
            invalid_entries.append((val, note))

    average = calculate_average(valid_readings)
    condition = classify_equipment(average)

    print("\n[Diagnostic Results]")
    print(f"Valid Readings: {len(valid_readings)} / {len(raw_data)}")
    print(f"Calculated Average: {average:.2f}")
    print(f"Equipment Condition: {condition}")

    print("\n[Execution Log]")
    print(f"Total Entries Processed: {len(raw_data)}")
    print(f"Valid: {len(valid_readings)} | Invalid: {len(invalid_entries)}")
    print("=" * 55)
    print("FINAL OUTPUT:", condition)
    print("=" * 55)

if __name__ == "__main__":
    main()