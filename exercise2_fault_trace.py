# EXERCISE 2: Recursive Fault Trace

# ==========================================
# STUDENT-SPECIFIC INPUTS — EDIT HERE
# ==========================================
LAST_NAME = "VIANA"
SEED_NUM = 3  # Last digit of TUPM-26-1953
FAVORITE_ARTIST = "BTS"  # ← SAME AS EXERCISE 1

# ==========================================
# 1. Generate Fault Code
# ==========================================
def generate_fault_code():
    name_sum = sum(ord(c) for c in LAST_NAME)
    artist_sum = sum(ord(c) for c in FAVORITE_ARTIST.replace(" ", ""))
    fault_code = (name_sum * SEED_NUM + artist_sum) % 10000
    return fault_code

# ==========================================
# 2. Recursive Fault Tracer
# ==========================================
call_count = 0
trace_log = []

def trace_fault(code, depth=1):
    global call_count
    call_count += 1

    # Base Condition — STOP
    if code < 100 or depth > 10:
        entry = f"[Depth {depth}] Code {code} → TERMINAL STATE"
        trace_log.append(entry)
        print(entry)
        return code

    # Recursive Step — CONTINUE
    entry = f"[Depth {depth}] Code {code} → Processing..."
    trace_log.append(entry)
    print(entry)
    new_code = code // 10
    return trace_fault(new_code, depth + 1)

# ==========================================
# MAIN PROGRAM
# ==========================================
def main():
    global call_count, trace_log
    call_count = 0
    trace_log = []

    print("=" * 55)
    print("RECURSIVE FAULT TRACE SYSTEM")
    print(f"Operator: {LAST_NAME} | Seed: {SEED_NUM}")
    print("=" * 55)

    fault_code = generate_fault_code()
    print(f"\n[Generated Fault Data]")
    print(f"Fault Code: {fault_code}")
    print(f"Derived From: Surname + Seed + Artist Name")

    print("\n[Recursive Trace]")
    final_state = trace_fault(fault_code)

    print(f"\n[Analysis]")
    print(f"Number of Recursive Calls: {call_count}")
    print(f"Base Condition Reached: Code < 100 or Depth > 10")

    print("\n[Execution Log]")
    for line in trace_log:
        print(f"  {line}")

    print("\n" + "=" * 55)
    print(f"FINAL OUTPUT: Terminal State {final_state} | Total Calls: {call_count}")
    print("=" * 55)

if __name__ == "__main__":
    main()