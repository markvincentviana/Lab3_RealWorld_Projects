# EXERCISE 3: Intelligent Equipment Monitoring Pipeline
import telemetry_core as core

# ==========================================
# STUDENT-SPECIFIC INPUTS — EDIT HERE
# ==========================================
LAST_NAME = "VIANA"
SEED_NUM = 3
FAVORITE_ARTIST = "BTS"  # ← SAME AS BEFORE

# ==========================================
# MAIN PROGRAM
# ==========================================
@core.monitor_processing
def main():
    print("=" * 60)
    print("INTELLIGENT EQUIPMENT MONITORING PIPELINE")
    print(f"Operator: {LAST_NAME} | Seed: {SEED_NUM}")
    print("=" * 60)

    # Generate stream length from artist name
    stream_length = len(FAVORITE_ARTIST.replace(" ", "")) + SEED_NUM
    print(f"\n[Student-Specific Inputs]")
    print(f"Stream Length: {stream_length} readings")

    print("\n[Generated Telemetry Data]")
    raw_readings = list(core.telemetry_stream(stream_length, SEED_NUM))
    print(f"Raw Stream: {raw_readings}")

    # Lambda transformation
    transformed = [core.transform_value(v) for v in raw_readings]
    average = sum(transformed) / len(transformed)
    print(f"\n[Processed Results]")
    print(f"Transformed Data: {transformed}")
    print(f"Stream Average: {average:.2f}")

    # Validation & abnormality detection
    valid_count = 0
    invalid_count = 0
    abnormal_readings = []

    print("\n[Validation Results]")
    for idx, val in enumerate(transformed, 1):
        try:
            if val < 0 or val > 100:
                raise ValueError(f"Out of bounds: {val}")
            valid_count += 1
            if core.is_abnormal(val, average):
                abnormal_readings.append((idx, val))
                print(f"  Reading {idx}: {val} ⚠ ABNORMAL")
            else:
                print(f"  Reading {idx}: {val} ✓ OK")
        except Exception as e:
            invalid_count += 1
            print(f"  Reading {idx}: {val} ✗ INVALID — {e}")

    # Recursive analysis
    print("\n[Recursive Analysis]")
    for idx, val in abnormal_readings:
        result = core.analyze_condition(val, average)
        print(f"  Reading {idx}: {result}")

    # Final report
    status = "OPERATIONAL" if valid_count > invalid_count else "REQUIRES INSPECTION"
    print("\n" + "=" * 60)
    print("[Final Diagnostic Summary]")
    print(f"Total Readings: {len(transformed)}")
    print(f"Valid: {valid_count} | Invalid: {invalid_count}")
    print(f"Abnormal Detected: {len(abnormal_readings)}")
    print(f"Overall Status: {status}")
    print("=" * 60)
    print("FINAL OUTPUT:", status)
    print("=" * 60)

if __name__ == "__main__":
    main()